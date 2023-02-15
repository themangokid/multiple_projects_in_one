import svgwrite
import math


# Set up the SVG canvas
drawing = svgwrite.Drawing(filename='../yearly.svg', size=(800, 800), viewBox="0 0 800 800")

# Draw the outer circle
outer_circle = drawing.circle(center=(400, 400), r=300, fill='white', stroke='black', stroke_width=2)
drawing.add(outer_circle)

# Draw the inner circle
inner_circle = drawing.circle(center=(400, 400), r=200, fill='white', stroke='black', stroke_width=2)
drawing.add(inner_circle)

# Define the colors for each month
colors = ['#ffc0cb', '#ffff00', '#00ff00', '#00ffff', '#800080', '#ff00ff', '#ff0000', '#ffa500', '#008000', '#000080', '#ff69b4', '#000000']

# Draw the months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i, month in enumerate(months):
    angle = 300 - i * 30  # 30 degrees per month
    x = 400 + 350 * math.cos(math.radians(angle))
    y = 400 + 350 * math.sin(math.radians(angle))
    text = drawing.text(month, insert=(x, y), font_size=30, text_anchor='middle')
    drawing.add(text)

    # Draw the stroke for this month's section
    section = drawing.path(d="M 400,400 L {} {} A 350,350 0 0,1 {} {} Z".format(400 + 350 * math.cos(math.radians(angle)), 400 + 350 * math.sin(math.radians(angle)), x, y), fill=colors[i], stroke='black', stroke_width=2)
    drawing.add(section)

# Save the drawing
drawing.save()
