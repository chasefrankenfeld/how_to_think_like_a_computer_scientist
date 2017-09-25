from unit_tester import test


class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs.
        The values of mins and secs may be outside the range 0-59,
        but the resulting MyTime object will be normalised.
        """
        # Calculate total seconds
        total_seconds = hrs * 3600 + mins * 60 + secs
        self.hours = total_seconds // 3600
        leftoversecs = total_seconds % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    # Question 4
    def increment(self, seconds):
        return MyTime(0, 0, self.to_seconds() + seconds)

    def to_seconds(self):
        """
        Return the number of seconds represented by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    # Version 1
    def after(self, time2):
        """ Return True if I am stricly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    # Question 3 - Over load the operaters greater than and greater than equal to
    # A replacement for after()
    def __gt__(self, time2):
        """ Return True if I am stricly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    # Question 2
    def between(self, other1, other2):
        if other1.to_seconds() <= self.to_seconds() and self.to_seconds() < other2.to_seconds():
            return True
        if other2.to_seconds() <= self.to_seconds() and self.to_seconds() < other1.to_seconds():
            return True
        return False


def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)

# Polymorphic examples
def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))

# Question 1
def between(t1, t2, obj):
    return t1.to_seconds() <= obj.to_seconds() and obj.to_seconds() < t2.to_seconds()

# Question 5 - test cases for increment, including those of negative seconds
# The negative seconds can never be more than the time object
test(str(MyTime(10,10,10).increment(10)) == str(MyTime(10,10,20)))
test(str(MyTime(10,10,10).increment(100)) == str(MyTime(10,11,50)))
test(str(MyTime(10,10,10).increment(-20)) == str(MyTime(10,9,50)))
test(str(MyTime(10,10,10).increment(-100)) == str(MyTime(10,8,30)))
