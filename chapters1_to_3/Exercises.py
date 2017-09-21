import math
import turtle


def draw_square(turt, sz):
    for i in range(4):
        turt.forward(sz)
        turt.left(90)


def create_turtle(clr, sz):
    t = turtle.Turtle()
    t.color(clr)
    t.pensize(sz)
    return t


wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = create_turtle("hotpink", 3)


def draw_five_squares(turt, sz):
    # Distance apart and the size of the
    for i in range(5):
        draw_square(turt, sz)
        alex.penup()
        alex.forward(sz * 2)
        alex.pendown()

def four_squares_within_a_square(turt, sz):
    for i in range(5):
        draw_square(turt, sz)
        turt.penup()
        turt.right(90)
        turt.forward(20)
        turt.right(90)
        turt.forward(20)
        turt.right(180)
        turt.pendown()
        sz += 20*2

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left((360/n))


def draw_2_squares(turt, sz):
    for i in range(2):
        draw_square(turt, sz)
        turt.forward(sz)

def draw_4_squares(turt, sz):
    draw_2_squares(turt, sz)
    turt.left(180)
    turt.forward(sz*2)
    turt.left(90)
    turt.forward(sz)
    turt.left(90)
    draw_2_squares(turt, sz)



def square_pattern(turt, sz):  # Need to fix this code.... Doesn't work as should
    for i in range(5):
        draw_4_squares(turt, sz)
        turt.penup()
        turt.right(90)
        turt.forward(sz/5)
        turt.left(90)
        turt.forward(sz/5)
        turt.right(90/5)
        turt.pendown()


def area_of_circle(r):
    area = math.pi * r**2
    return area

def drawing_5_pointed_star(turt, sz):
    for i in range(5):
        turt.forward(sz)
        turt.right(144)

def drawing_5_stars(turt, sz):
    for i in range(5):
        drawing_5_pointed_star(turt, sz)
        #turt.penup()
        turt.forward(sz * (7/2))
        turt.right(144)
        #turt.pendown()


#draw_five_squares(alex, 40)
#four_squares_within_a_square(alex, 20)
#draw_poly(alex, 3, 50)
#square_pattern(alex, 100)
#print(area_of_circle(10))

drawing_5_stars(alex, 20)

wn.mainloop()
