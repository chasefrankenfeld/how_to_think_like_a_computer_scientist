import turtle

xs = [48, 117, 200, -100, 240, - 10, 160, 260, 220]

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)


def draw_bar(t, height):
    """Get turtle t to draw one bar, on height."""
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


def draw_bar_backwards(t, height):
    """Get turtle t to draw one bar, on height."""
    t.begin_fill()
    t.right(90)
    t.forward(-height)
    t.left(90)
    t.forward(40)
    t.write("  " + str(height), align="left") #attempting to write the number below the bar chart. Cannot figure it out.
    t.left(90)
    t.forward(-height)
    t.right(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


for v in xs:
    if v >= 200:
        tess.color("blue", "red")
        draw_bar(tess, v)
    elif v >= 100:
        tess.color("blue", "yellow")
        draw_bar(tess, v)
    elif v >= 0:
        tess.color("blue", "green")
        draw_bar(tess, v)
    else:
        tess.color("blue", "green")
        draw_bar_backwards(tess, v)

wn.mainloop()
