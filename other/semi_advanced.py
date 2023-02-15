import svgwrite
import math


# Set up the SVG canvas
drawing = svgwrite.Drawing(filename='yearly.svg', size=(600, 600), viewBox="0 0 600 600")

# Draw the outer circle
outer_circle = drawing.circle(center=(300, 300), r=250, fill='white', stroke='black', stroke_width=2)
drawing.add(outer_circle)

# Draw the inner circle
inner_circle = drawing.circle(center=(300, 300), r=200, fill='white', stroke='black', stroke_width=2)
drawing.add(inner_circle)

# Draw the months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i, month in enumerate(months):
    angle = i * 30  # 30 degrees per month
    x = 300 + 180 * math.cos(math.radians(angle))
    y = 300 + 180 * math.sin(math.radians(angle))
    text = drawing.text(month, insert=(x, y), font_size=30, text_anchor='middle')
    drawing.add(text)

# Save the drawing
drawing.save()
