from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
socketio = SocketIO(app)

# create a set of authorized clients (just the server admin initially)
authorized_clients = ['localhost']

@app.route('/')
def index():
    # check if the user is authorized to view the slide show
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('my-slide-show.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # check if the password is correct
        username = request.form['username']
        password = request.form['password']
        if password == 'my-password':
            # add the user to the set of authorized clients
            authorized_clients.append(request.remote_addr)
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@socketio.on('slide_change')
def handle_slide_change(slide_number):
    # check if the client is authorized to change slides
    if request.remote_addr in authorized_clients:
        send(slide_number, broadcast=True)

@socketio.on('slide change')
def handle_slide_change(slide_number):
    emit('slide changed', slide_number, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)


@app.route('/logout')
def logout():
    # remove the user from the set of authorized clients
    authorized_clients.pop(request.remote_addr)
    session.pop('username', None)
    return redirect(url_for('login'))
