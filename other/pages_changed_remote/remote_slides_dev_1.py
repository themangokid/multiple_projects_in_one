from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('my-slide-show.html')

@socketio.on('slide change')
def handle_slide_change(slide_number):
    emit('slide changed', slide_number, broadcast=True)

@socketio.on('key press')
def handle_key_press(key_code):
    current_slide = 1  # Replace with your own default slide number
    if key_code == 'ArrowRight':
        current_slide += 1
    elif key_code == 'ArrowLeft':
        current_slide -= 1
    emit('slide changed', current_slide, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
