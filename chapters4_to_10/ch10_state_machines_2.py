import turtle


turtle.setup(400, 500)              # Determine the window size
wn = turtle.Screen()                # Get a reference to the window
wn.title("Handling keypresses!")    # Change the window title
wn.bgcolor("lightgreen")            # Set the background color
tess = turtle.Turtle()              # Create two turtles
green = "green"
lightgreen = "lightgreen"

kayla = turtle.Turtle()
orange = "orange"
lightorange = "lightorange"

kara = turtle.Turtle()
red = "red"
lightred = "lightred"


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()


def draw_light(name, clr):
    name.shape("circle")
    name.shapesize(3)
    name.fillcolor(clr)


def unglow(name):
    name.fillcolor("")


def glow(name, clr):
    name.fillcolor(clr)


# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess's position and
# her fillcolor

def green_light(name, clr):
    name.penup()
    # Position tess onto the place where the green light shoulld be
    name.forward(40)
    name.left(90)
    name.forward(50)
    # Turn tess into a big green circle
    draw_light(name, clr)


def orange_light(name, clr):
    name.penup()
    name.forward(40)
    name.left(90)
    name.forward(120)
    # Turn kayla into a big green circle
    draw_light(name, clr)
    #hide_turtle(name)
    unglow(name)


def red_light(name, clr):
    name.penup()
    name.forward(40)
    name.left(90)
    name.forward(190)
    # Turn kara into a big green circle
    draw_light(name, clr)
    #hide_turtle(name)
    unglow(name)


# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to 1
        #show_turtle(kayla)
        glow(kayla, orange)
        state_num = 1
    elif state_num == 1:
        unglow(tess)
        # show_turtle(kayla)
        glow(kayla, orange)
        state_num = 2
    elif state_num == 2:  # Transition from state 1 to 2
        unglow(kayla)
        #show_turtle(kara)
        glow(kara, red)
        state_num = 3
    else:  # Transition from state 2 to 0
        unglow(kara)
        #show_turtle(tess)
        glow(tess, green)
        state_num = 0


def hide_turtle(name):
    name.hideturtle()


def show_turtle(name):
    name.showturtle()

green_light(tess, green)
orange_light(kayla, orange)
red_light(kara, red)


# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                     # Listen to events
wn.mainloop()
