import turtle

def make_window(colr, ttle):
    """
        Set up the window with the given backgroun color and title.
        Returns a new window
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    """
        Set up a turtle with a given color and pensize/
        Returns the new turtle
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen", "Drunken Pirate")
tess = make_turtle("red", 2)

# chapter 7 exercises

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
steps_and_turns = [(160, 20), (-43, 10), (270, 8), (-43, 12)]


def drunken_pirate(t, x):
    for i in x:
        t.left(i)
        t.forward(100)


def drunken_pirate_2(t, x):
    for (angle, dist) in x:
        t.left(angle)
        t.forward(dist)


# Exercise 12

exercise_12 = [(0, 100),
               (135, (2 * (100 ** 2))**(1/2)),
               (135, 100),
               (135, (2 * (100 ** 2))**(1/2)),
               (135, 100),
               (-135, ((100**2)/2)**(1/2)),
               (-90, ((100**2)/2)**(1/2)),
               (-45, 100)]


exercise_13_a = [(0, 100), (90, 100), (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-135, 100),
                 (90, 100)]


exercise_13_b = [(0, 100),
                 (90, 100),
                 (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-135, 100),
                 (135, (2 * (100 ** 2))**(1/2)),
                 (-135, 100),
                 (-90, 100)]


exercise_13_c = [(0, 100), (90, 100), (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-135, 100),
                 (90, 100),
                 (135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2))
                 ]

exercise_13_d = [(0, 100), (90, 100), (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-135, 100),
                 (90, 100),
                 (135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (180, (2 * (100 ** 2))**(1/2))
                 ]


exercise_13_e = [(0, 100), (90, 100), (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-135, 100),
                 (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-45, 100),
                 (-45, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2))
                 ]


exercise_13_f = [(0, 100),
                 (90, 100),
                 (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-135, 100),
                 (90, 100),
                 (-135, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-45, 100),
                 (-45, ((100**2)/2)**(1/2)),
                 (-90, ((100**2)/2)**(1/2)),
                 (-90, (2 * (100 ** 2))**(1/2)),
                 (-135, 100),
                 (-135, (2 * (100 ** 2))**(1/2))
                 ]


#drunken_pirate(tess, turns)
#drunken_pirate_2(tess, steps_and_turns)
#drunken_pirate_2(tess, exercise_12)
#drunken_pirate_2(tess, exercise_13_a)
#drunken_pirate_2(tess, exercise_13_b)
#drunken_pirate_2(tess, exercise_13_c)
#drunken_pirate_2(tess, exercise_13_d)
#drunken_pirate_2(tess, exercise_13_e)
drunken_pirate_2(tess, exercise_13_f)


wn.mainloop()