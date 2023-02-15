import math
import svgwrite




# Size of the yearly wheel
size = 600

# Month names and colors
month_names = [
    ('January', '#f2c057'),
    ('February', '#8da0cb'),
    ('March', '#e78ac3'),
    ('April', '#a6d854'),
    ('May', '#ffd92f'),
    ('June', '#e5c494'),
    ('July', '#b3b3b3'),
    ('August', '#c7eae5'),
    ('September', '#ad494a'),
    ('October', '#00bfff'),
    ('November', '#a1caf1'),
    ('December', '#8fb6d2'),
]

# Create a new SVG drawing
drawing = svgwrite.Drawing(filename='yearly.svg', size=(size, size))

# Define the center of the circle
center = size / 2

# Define the radius of the circle
radius = size / 2 - 20

# Loop through each month
for i, (name, color) in enumerate(month_names):

    # Calculate the angle for the start and end of the month
    start_angle = 2 * math.pi * i / 12
    end_angle = 2 * math.pi * (i + 1) / 12

    # Calculate the coordinates for the start and end of the month
    x1 = center + radius * math.sin(start_angle)
    y1 = center - radius * math.cos(start_angle)
    x2 = center + radius * math.sin(end_angle)
    y2 = center - radius * math.cos(end_angle)

    # Draw the month as a circle
    drawing.add(svgwrite.Drawing(center=(x1 + x2) / 2, r=20, fill=color))

    # Draw the name of the month
    text = drawing.add(drawing.text(name, insert=(center, center), fill='#000', font_size=24, text_anchor='middle'))
    text.rotate(30 * i, center=(center, center))

# Save the drawing to a file
drawing.save()
