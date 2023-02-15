import svgwrite
import math


def draw_yearly_calendar(size, font, colors):
    # Set up the SVG canvas
    drawing = svgwrite.Drawing(filename='../yearly.svg', size=size, viewBox=f"0 0 {size[0]} {size[1]}")

    # Draw the outer circle
    outer_circle = drawing.circle(center=(size[0] // 2, size[1] // 2), r=size[0] * 0.4, fill='white', stroke='black',
                                  stroke_width=2)
    drawing.add(outer_circle)

    # Draw the inner circle
    inner_circle = drawing.circle(center=(size[0] // 2, size[1] // 2), r=size[0] * 0.33, fill='white', stroke='black',
                                  stroke_width=2)
    drawing.add(inner_circle)

    # Draw the months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i, month in enumerate(months):
        angle = i * 30  # 30 degrees per month
        x = size[0] // 2 + size[0] * 0.17 * math.cos(math.radians(angle))
        y = size[1] // 2 + size[0] * 0.17 * math.sin(math.radians(angle))
        text = drawing.text(month, insert=(x, y), font_size=40, text_anchor='middle', font_family=font, fill=colors[i])
        drawing.add(text)

    # Save the drawing
    drawing.save()


colors = ['#FF4136', '#FF851B', '#FFDC00', '#2ECC40', '#0074D9', '#B10DC9', '#01FF70', '#7FDBFF', '#F012BE', '#3D9970',
          '#39CCCC', '#85144b']
draw_yearly_calendar((800, 800), 'Arial', colors)
