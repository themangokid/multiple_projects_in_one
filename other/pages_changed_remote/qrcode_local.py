from flask import Flask, render_template
import qrcode
import socket

app = Flask(__name__)

# Get the local IP address of the machine
local_ip = socket.gethostbyname(socket.gethostname())

# Generate a random port number between 5000 and 9999
port = 5000 + hash(local_ip) % 5000

# Define a route that generates the QR code
@app.route('/qr')
def qr():
    # Generate a random seed
    seed = hash(local_ip) % 10000

    # Generate the URL for the application
    url = f"http://{local_ip}:{port}/{seed}"

    # Generate the QR code using the url
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color='black', back_color='white')

    # Return the rendered HTML template with the QR code image
    return render_template('qr.html', qr=qr_image)

# Define a route that displays the slide show
@app.route('/<int:seed>')
def slide_show(seed):
    # Here you can generate the slide show based on the seed
    # For this example, we just return some static content
    return render_template('slide_show.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run(host=local_ip, port=port)