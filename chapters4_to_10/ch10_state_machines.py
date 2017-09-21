import turtle


turtle.setup(400, 500)              # Determine the window size
wn = turtle.Screen()                # Get a reference to the window
wn.title("Handling keypresses!")    # Change the window title
wn.bgcolor("lightgreen")            # Set the background color
tess = turtle.Turtle()              # Create two turtles


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

tess.penup()
# Position tess onto the place where the green light shoulld be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess's position and
# her fillcolor

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine_timer():
    global state_num
    if state_num == 0:          # Transition from state 0 to 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine_timer, 1000)
    elif state_num == 1:        # Transition from state 1 to 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine_timer, 1000)
    else:                       # Transition from state 2 to 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine_timer, 1000)

def advance_state_machine_onkey():
    global state_num
    if state_num == 0:  # Transition from state 0 to 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:  # Transition from state 2 to 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


# Bind the event handler to the space key.
#wn.ontimer(advance_state_machine_timer, 1000)
wn.onkey(advance_state_machine_onkey, "space")

wn.listen()                     # Listen to events
wn.mainloop()
