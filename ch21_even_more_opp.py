class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting
        """

        # Calculate total seconds to reporesent
        total_secs = hrs*3600 + mins*60 + secs
        self.hours = total_secs // 3600  # Split into h, m, s
        leftovers = total_secs % 3600
        self.minutes = leftovers // 60
        self.seconds = leftovers % 60

    def __str__(self):
        return "The time is {0}:{1}:{2}".\
            format(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def increment(self, secs):
        self.seconds += secs

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

tim1 = MyTime(11, 59, 30)
tim2 = MyTime(1, 1, 1)
t3 = tim1 + tim2
print(t3)
t4 = t3 - tim2
print(t4)
#tim1.increment(500)
#print(tim1)


def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)

#rint(add_time(tim1, tim2))