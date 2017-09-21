import turtle

import os


def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returns just the names, not full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix=""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outerost call, path a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)  # Print the line
        fullname = os.path.join(path, f)  # Turn name into full pathname
        if os.path.isdir(fullname):  # If director, recurse
            print_files(fullname, prefix + "| ")


# print_files("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pygame/examples/")

screen = turtle.Screen()
screen.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")


def koch_0(t, size):
    t.forward(size)


def koch_1(t, size):
    for angle in [60, -120, 60, 0]:
        koch_0(t, size / 3)
        t.left(angle)


def koch_2(t, size):
    for angle in [60, -120, 60, 0]:
        koch_1(t, size / 3)
        t.left(angle)


def koch_3(t, size):
    for angle in [-120, -120, 0]:
        koch_2(t, size / 3)
        t.left(angle)


# koch_3(tess, 200)

def cesaro_0(t, size):
    t.forward(size)


def cesaro_1(t, size):
    for angle in [85, -170, 85, 0]:
        cesaro_0(t, size)
        t.right(angle)


def cesaro_2(t, size):
    for angle in [85, -170, 85, 0]:
        cesaro_1(t, size)
        t.right(angle)


def cesaro_3(t, size):
    for angle in [85, -170, 85, 0]:
        cesaro_2(t, size)
        t.right(angle)


# cesaro_3(tess, 25)

def cesaro_square(t, size):
    for x in range(4):
        cesaro_3(t, size)
        t.right(90)


# cesaro_square(tess, 25)

def triangle(t, size):
    t.forward(size)


def triangle_1(t, size):
    for angle in [120, 120, 120]:
        triangle(t, size)
        t.left(angle)


def triangle_2(t, size):
    triangle_1(t, size)

    t.penup()
    t.forward(size)
    t.pendown()

    triangle_1(t, size)

    t.penup()
    t.left(120)
    t.forward(size)
    t.left(-120)
    t.pendown()

    triangle_1(t, size)

    t.penup()
    for x in [60, -60]:
        t.forward(size)
        t.right(x)
    t.pendown()


def move_to_third_triangle(t, size):
    t.penup()
    for x in [120, 60]:
        t.left(x)
        t.forward(size)
    t.left(180)
    t.pendown()


def move_to_start_new_triangle(t, size):
    t.penup()
    t.right(60)
    t.forward(size)
    t.left(60)
    t.pendown()


def triangle_3(t, size):
    triangle_2(t, size / 2)

    triangle_2(t, size / 2)

    move_to_third_triangle(t, size)

    triangle_2(t, size / 2)

    move_to_start_new_triangle(t, size)


def triangle_4(t, size, colorChangeDepth=-1):
    if colorChangeDepth == -1:
        t.color("black")
    elif colorChangeDepth == 0:
        t.color("red")
    triangle_3(t, size / 2)

    if colorChangeDepth == -1:
        t.color("black")
    elif colorChangeDepth == 0:
        t.color("blue")
    triangle_3(t, size / 2)

    move_to_third_triangle(t, size)

    if colorChangeDepth == -1:
        t.color("black")
    elif colorChangeDepth == 0:
        t.color("magenta")
    triangle_3(t, size / 2)

    move_to_start_new_triangle(t, size)


def triangle_5(t, size, colorChangeDepth=-1):
    triangle_4(t, size / 2, colorChangeDepth)

    triangle_4(t, size / 2, colorChangeDepth)

    move_to_third_triangle(t, size)

    triangle_4(t, size / 2, colorChangeDepth)

    move_to_start_new_triangle(t, size)


def triangle_6(t, size, colorChangeDepth=-1):
    triangle_5(t, size / 2, colorChangeDepth)

    triangle_5(t, size / 2, colorChangeDepth)

    move_to_third_triangle(t, size)

    triangle_5(t, size / 2, colorChangeDepth)

    move_to_start_new_triangle(t, size)


triangle_6(tess, 200, 0)

screen.mainloop()