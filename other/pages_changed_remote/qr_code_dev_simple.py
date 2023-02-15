import qrcode
import svgwrite

# Define the seed value for the QR code
seed_value = 'my_secret_seed'

# Generate the QR code data
qr_data = qrcode.QRCode(1, 40)

# Generate the QR code as a SVG image
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qr_data)
qr.make(fit=True)

svg_image = svgwrite.Drawing(filename='qrcode.svg', size=(qr.modules_count * 10, qr.modules_count * 10))
svg_image.saveas("qrcode.svg")


for row in range(qr.modules_count):
    for col in range(qr.modules_count):
        if qr.modules[row][col]:
            x, y = col * 10, row * 10
            svg_image.add(svgwrite.Drawing(insert=(x, y), size=(10, 10), fill='black'))

svg_image.save()
