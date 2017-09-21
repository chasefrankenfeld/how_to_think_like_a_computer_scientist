import turtle

turtle.setup(400, 500)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("Handling keypresses!")  # Change the window title
wn.bgcolor("lightgreen")  # Set the background color

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)


def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 60)


h1()
wn.mainloop()
