import turtle


turtle.setup(400, 500)              # Determine the window size
wn = turtle.Screen()                # Get a reference to the window
wn.title("Handling keypresses!")    # Change the window title
wn.bgcolor("lightgreen")            # Set the background color

tess = turtle.Turtle()              # Create our favourite turtle
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

def h1(x, y):
    wn.title("Got click at coord {0}, {1}".format(x,y))
    tess.goto(x, y)                 # This move the turtle to an absolute coordinate

wn.onclick(h1)                      # Wire up a click on the window
wn.mainloop()