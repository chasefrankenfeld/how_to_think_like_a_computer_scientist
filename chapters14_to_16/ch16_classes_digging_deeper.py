import sys


def test(did_pass):
    """ Print the rests of the test """
    linenum = sys._getframe(1).f_lineno  # gets the callers line number
    if did_pass:
        msg = "Test at line {} is ok.".format(linenum)
    else:
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)


class Point:
    """ Point class represents and manipulates x, y coordinates. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y. """
        self.x = x
        self.y = y

    def __str__(self):
        """ Converting the point to a string. """
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distance_from_origin(self):
        """ Compute m distance from the origin. """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def reflex_x(self):
        """ Reflecting the point in the x-axis """
        mx = self.x
        my = self.y
        return mx, -my

    def slope_from_origin(self):
        """ Returns the slop of the line joining the origin to the point """
        return self.y / self.x

    def straight_line_points(self, target):
        """ Returns the values m and c from y = mx + c """
        m = ((self.y - target.y) / (self.x - target.x))
        c = self.y - m * self.x
        return m, c


class Rectangle:
    """ A classes to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialise the rectange at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move the point by dx and dy """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """ Return the area of the rectangle """
        return self.height * self.width

    def perimeter(self):
        """ Return the length of the perimeter """
        return self.width * 2 + self.height * 2

    def flip(self):
        """ Swap the width and height lengths """
        x = self.height
        y = self.width
        self.height = y
        self.width = x

    def contains(self, point):
        """ Test if a point falls with in the rectangle """
        outer_x = self.corner.x + self.width
        outer_y = self.corner.y + self.height
        return (self.corner.x <= point.x < outer_x and
                self.corner.y <= point.y < outer_y)

    def collision(self, other):
        """ Test if another rectangle collides with the first rectangle. """
        outer_x = self.corner.x + self.width
        outer_y = self.corner.y + self.height
        if (self.corner.x <= other.corner.x <= outer_x and
            self.corner.y <= other.corner.y <= outer_y):
            return True
        if (self.corner.x <= other.corner.x + other.width <= outer_x and
            self.corner.y <= other.corner.y + other.height <= outer_y):
            return True
        if (self.corner.x <= other.corner.x <= outer_x and
            self.corner.y <= other.corner.y + other.height <= outer_y):
            return True
        if (self.corner.x <= other.corner.x + other.width <= outer_x and
            self.corner.y <= other.corner.y <= outer_y):
            return True
        return False


def test_suite():
    r = Rectangle(Point(0, 0), 10, 5)

    test(r.area() == 50)

    test(r.perimeter() == 30)

    test(r.width == 10 and r.height == 5)
    #r.flip()
    #test(r.width == 5 and r.height == 10)

    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))

    # Testing if collision with the point of the Other Rectangle
    test(r.collision(Rectangle(Point(0, 0), 10, 5)))
    test(r.collision(Rectangle(Point(5, 0), 10, 5)))
    test(r.collision(Rectangle(Point(10, 5), 10, 5)))
    test(r.collision(Rectangle(Point(9, 4), 10, 5)))
    test(not r.collision(Rectangle(Point(20, 5), 10, 5)))

    # Testing if collision with the top right corner of Other Rectangle
    test(not r.collision(Rectangle(Point(-11, 5), 10, 5)))
    test(r.collision(Rectangle(Point(0, 0), 10, 5)))
    test(not r.collision(Rectangle(Point(0, -6), 10, 5)))
    test(r.collision(Rectangle(Point(-9, -4), 10, 5)))

    # Testing if collision with the top left corner of Other Rectangle
    test(r.collision(Rectangle(Point(10, -5), 10, 5)))
    test(not r.collision(Rectangle(Point(10, -6), 10, 5)))

    # Testing if collision with the bottom right corner of Other Rectangle
    test(r.collision(Rectangle(Point(-10, 5), 10, 5)))
    test(not r.collision(Rectangle(Point(-11, 0), 10, 5)))



test_suite()
