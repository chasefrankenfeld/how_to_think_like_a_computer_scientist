class Point:
    """ Point class represents and manipulates x, y coordinates. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y. """
        self.x = x
        self.y = y

    def __str__(self):
        """ Converting the point to a string. """
        return "({0}, {1})".format(self.x, self.y)

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


class SMS_store:
    """ Hold a list of messages that are represented as a tuple """

    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, test_of_SMS):
        """ Makes new SMS tuple, inserts it after other messages
            in the store. has_been_viewed status is set to False.
        """
        self.messages.append((False, from_number, time_arrived, test_of_SMS))

    def message_count(self):
        """ Returns the  number of messages in the inbox created """
        return len(self.messages)

    def get_unread_indexes(self):
        """ Returns list of indexes of all not-yet-viewed SMS messages """
        unread = []
        for (i, x) in enumerate(self.messages):
            if not x[0]:
                unread.append(i)
        return unread

    def get_message(self, i):
        """ Return (from_number, time_arrived, test_of_SMS for message[i]
            Also change its state to "has been viewed".
            If there is no message at position i, return None.
        """
        try:
            return self.messages[i][1:]
        except IndexError:
            return None

    def delete(self, i):
        """ Delete the messages at index i """
        del self.messages[i]

    def clear(self):
        """ Delete all messages from the inbox """
        self.messages = []


# Other statements outside the class continue below here.

