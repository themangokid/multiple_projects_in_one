import svgwrite

# Create an SVG drawing with size 100x100
drawing = svgwrite.Drawing(filename='simple.svg', size=(100, 100))

# Draw a rectangle with top-left corner at (10, 10) and size (80, 80)
drawing.add(drawing.rect(insert=(10, 10), size=(80, 80)))

# Save the drawing to a file
drawing.save()
