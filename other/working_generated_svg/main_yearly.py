import svgwrite
import math


# https://svgwrite.readthedocs.io/en/latest/classes/mixins.html

def draw_month_wheel(filename, size=(800, 800), viewbox="0 0 800 800", stroke_width=2,
                     outer_circle_radius=350, inner_circle_radius=300, font_family="Arial",
                     font_size=30, font_weight="normal", font_color="#000000"):
    # Set up the SVG canvas
    drawing = svgwrite.Drawing(filename=filename, size=size, viewBox=viewbox)

    # Draw the outer circle
    outer_circle = drawing.circle(center=(size[0] / 2, size[1] / 2), r=outer_circle_radius,
                                  fill='white', stroke='#000000', stroke_width=stroke_width)
    drawing.add(outer_circle)

    # Draw the inner circle
    inner_circle = drawing.circle(center=(size[0] / 2, size[1] / 2), r=inner_circle_radius,
                                  fill='white', stroke='#000000', stroke_width=stroke_width)
    drawing.add(inner_circle)

    # Draw the months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i, month in enumerate(months):
        angle = 30 * (i - 2)  # shift starting point to left-center
        x = (size[0] / 2) + (outer_circle_radius + 20) * math.cos(math.radians(angle))
        y = (size[1] / 2) + (outer_circle_radius + 20) * math.sin(math.radians(angle))
        text = drawing.text(month, insert=(x, y), font_family=font_family, font_size=font_size,
                            font_weight=font_weight, fill=font_color, text_anchor='middle')
        drawing.add(text)

    # Save the drawing
    drawing.save()


# Example usage
draw_month_wheel("../yearly.svg", size=(800, 800), viewbox="0 0 0 0", stroke_width=3,
                 outer_circle_radius=250, inner_circle_radius=200, font_family="Helvetica",
                 font_size=36, font_weight="bold", font_color="#0066cc")
