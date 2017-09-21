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

    def reverse(self):
        (self.x, self.y) = (self.y, self.x)

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