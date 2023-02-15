import svgwrite

WIDTH = 800
HEIGHT = 800
RADIUS = 350

MONTHS = [    "december", "januari", "februari", "maart", "april", "mei", "juni",    "juli", "augustus", "september", "oktober", "november"]

def draw_yearly_calendar():
    dwg = svgwrite.Drawing('yearly_calendar.svg', profile='full')
    center = (WIDTH / 2, HEIGHT / 2)
    for i, month in enumerate(MONTHS):
        angle = i * (360 / len(MONTHS))
        radians = angle * 3.14159 / 180
        x = center[0] + RADIUS * (radians)
        y = center[1] + RADIUS * svgwrite.util.sin(radians)
        text = dwg.text(month.capitalize(), insert=(x, y), text_anchor="middle", font_size="30pt", font_family="Arial")
        dwg.add(text)
    dwg.save()

draw_yearly_calendar()
