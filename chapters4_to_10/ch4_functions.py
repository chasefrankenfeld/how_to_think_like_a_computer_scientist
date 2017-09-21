import turtle

def draw_square(t, sz):
    """Make the tutle t draw a square sq."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

def draw_rectangle(t, w, h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square_2(tx, sz):
    draw_rectangle(tx, sz, sz)

def draw_multicolor_square(t, sz):
    """Make a turtle t draw a multi-color square of sz"""
    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

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

wn = make_window("lightgreen", "Tess and alex")
tess = make_turtle("blue", 3)
alex = make_window("pink", 5)
dave = make_turtle("black", 1)


def cool_picture(bla, sizz):
    size = sizz
    for i in range(15):
        draw_multicolor_square(bla, size)
        size += 10
        bla.forward(10)
        bla.right(18)


def final_amount(p, r, n, t):
    a = p*(1+(r/n))**(n*t)
    return a

#toInvest = float(input("How much money do you want to invest? "))
#fnl = final_amount(toInvest, 0.08, 12, 10)
#print("At the end of the period, you'll have {}".format(fnl))

cool_picture(alex, 40)

wn.mainloop()