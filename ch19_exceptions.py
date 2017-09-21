import turtle
import time
import threading


def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age.".format(age))
        raise my_error
    return age


# get_age()


def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")


# recursion_depth(0)


def show_poly():
    try:
        win = turtle.Screen()  # Grab/create a resource, e.g. a window
        tess = turtle.Turtle()

        # This dialog wold be cancelled,
        # or the conversation to int might fail, or n might be zeor.
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):  # Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)  # Make the program wait a few seconds
    finally:
        win.bye()


# show_poly()
# show_poly()
# how_poly()


def readpostint():
    """ Check user input from prompt
        to see if it is a positive integer
        Should be able to handle inputs that cannot be
        converted into an int, as well as negative ints,
        and edge cases (when user closes the dialog box, or
        does not enter anything at all.
    """

    def exception():
        print("")
        print("Please enter a number: ")

    while True:
        try:
            t = threading.Timer(5, exception)
            t.start()
            pos_num = int(input("Insert a positive number: "))
            t.cancel()
        except ValueError:
            print("That is not a number. Please try again!")
            continue
        if pos_num < 0:
            print("The number must be positive.")
        else:
            return pos_num


readpostint()
