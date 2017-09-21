import random

import time

import calendar

import math

from unit_tester import test


def make_random_ints(num, lower_bound, upper_bound):
    """
    Generate a list containing num andom ints between lower_bound
    and upper_bound, upper_bound is an open bound
    """
    rng = random.Random()  # Create a random number generator
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result


def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. Upper_bound is an open bound.
    The result list cannot contain duplicates.
    """
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


# print(make_random_ints(5, 1, 13))
# xs = make_random_ints_no_dups(5, 1, 1000000)
# print(xs)


def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum


def time_module():
    sz = 10000000  # Lets have 10 million elements in the list
    testdata = range(sz)

    t0 = time.clock()
    my_result = do_my_sum(testdata)
    t1 = time.clock()
    print("my_result = {0} (time taken = {1:.4f} seconds)".format(my_result, t1 - t0))

    t2 = time.clock()
    their_result = sum(testdata)
    t3 = time.clock()
    print("thier_result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3 - t2))


# time_module()

# cal = calendar.TextCalendar()  # Create an instance
# calendar.setfirstweekday(2)
# print(calendar.firstweekday())
# cal.pryear(2012)
# cal.formatmonth(2016, 7)
# cal.prmonth(2016, 7)

# d = calendar.LocaleTextCalendar(6, "se_NO")
# d.pryear(2015)

# print(calendar.isleap(2012))

print(math.sqrt(25))


def square_roote(x):
    approx = x / 2.0
    while True:
        better = (approx + x / approx) / 2.0
        if abs(approx - better) < 0.00001:
            return better
        approx = better


def myreplace(old, new, s):
    """
        Replace all occurrences of old with the new in s.
    """
    return new.join(s.split(old))


def test_suite():
    # test(square_roote(25) == 5)
    test(myreplace(",", ";", "this, that, and some other thing") ==
         "this; that; and some other thing")
    test(myreplace(" ", "**", "Words will now be separated by stars.") ==
         "Words**will**now**be**separated**by**stars.")


test_suite()
