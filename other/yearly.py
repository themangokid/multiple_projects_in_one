import svgwrite

# Define the size and colors of the wheel
size = 500
background_color = 'white'
border_color = 'black'
text_color = 'black'

# Define the months and their corresponding colors
months = {
    'January': 'red',
    'February': 'orange',
    'March': 'yellow',
    'April': 'green',
    'May': 'blue',
    'June': 'purple',
    'July': 'pink',
    'August': 'brown',
    'September': 'gray',
    'October': 'navy',
    'November': 'teal',
    'December': 'maroon'
}

# Create the SVG drawing
drawing = svgwrite.Drawing('yearly_wheel.svg', size=(size, size))

# Draw the background and border
drawing.add(drawing.rect(insert=(0, 0), size=(size, size), fill=background_color))
drawing.add(drawing.circle(center=(size / 2, size / 2), r=(size / 2) - 10, fill='none', stroke=border_color, stroke_width=20))

# Draw the months as pie slices
angle = 0
angle_increment = 360 / len(months)
for month, color in months.items():
    drawing.add(drawing.path(
        d=f'M {size / 2},{size / 2} L {size / 2},{10} A {(size / 2) - 10, (size / 2) - 10, 0, 0, 1},'
          f'{size / 2 + ((size / 2) - 10) * (2 ** 0.5) * (angle + angle_increment / 2) / 360},'
          f'{size / 2 + ((size / 2) - 10) * (2 ** 0.5) * (angle + angle_increment / 2) / 360}) Z',
        fill=color))

    # Add the month name as text
    text_angle = angle + angle_increment / 2
    text_x = size / 2 + ((size / 2) - 50) * (2 ** 0.5) * text_angle / 360
    text_y = size / 2 + ((size / 2) - 50) * (2 ** 0.5) * text_angle / 360
    drawing.add(drawing.text(month, insert=(text_x, text_y), fill=text_color))
    angle += angle_increment

# Save the SVG drawing to a file
drawing.save()

# Prompt the user for a month and color to update
print('Enter a month and a color to update (e.g. January red):')
input_str = input()
input_list = input_str.split()
if len(input_list) != 2:
    print('Invalid input')
else:
    month = input_list[0]
    color = input_list[1]
    if month not in months:
        print('Invalid month')
    else:
        months[month] = color
        # Re-draw the SVG drawing with the updated months
        drawing = svgwrite.Drawing('yearly_wheel.svg', size=(size, size))
        drawing.add(drawing.rect(insert=(0, 0), size=(size, size), fill=background_color))
        drawing.add(drawing.circle(center=(size / 2, size / 2), r=(size / 2) - 10, fill='none', stroke=border_color, stroke_width = 20))
        angle = 0
        angle_increment = 360 / len(months)
        for month, color in months.items():
            drawing.add(drawing.path(
                d=f'M {size / 2},{size / 2} L {size / 2},{10} A {(size / 2) - 10, (size / 2) - 10, 0, 0, 1} ,'
                  f'{size / 2 + ((size / 2) - 10) * (2 ** 0.5) * (angle + angle_increment / 2) / 360},'
                  f'{size / 2 + ((size / 2) - 10) * (2 ** 0.5) * (angle + angle_increment / 2) / 360}) Z',
                fill=color))

            text_angle = angle + angle_increment / 2
            text_x = size / 2 + ((size / 2) - 50) * (2 ** 0.5) * text_angle / 360
            text_y = size / 2 + ((size / 2) - 50) * (2 ** 0.5) * text_angle / 360
            drawing.add(drawing.text(month, insert=(text_x, text_y), fill=text_color))
            angle += angle_increment
        drawing.save()
        print('Yearly wheel updated')










