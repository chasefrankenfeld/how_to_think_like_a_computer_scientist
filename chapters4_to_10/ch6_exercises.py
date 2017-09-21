import sys

import math


def test(did_pass):
    """Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Gets the caller's line number.
    if did_pass:
        msg = "Test at line {} ok.".format(linenum)
    else:
        msg = "Test at line {} FAILED.".format(linenum)
        print(msg)


def test_suite():
    """Run the suite of tests for code in this module (this file)."""
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)

    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")

    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)

    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)

    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)

    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)

    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)

    test(is_even(10))
    test(not is_even(7))
    test(not is_even(7))
    test(is_even(-6))

    test(not is_odd(10))
    test(is_odd(7))
    test(is_odd(7))
    test(not is_odd(-6))

    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))

    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

def turn_clockwise(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
    else:
        return None


def day_name(day_number):
    if day_number == 0:
        return "Sunday"
    elif day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    else:
        return None


def day_num(day_name):
    if day_name == "Sunday":
        return 0
    elif day_name == "Monday":
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == "Saturday":
        return 6
    return None


def day_add(day, days):
    return day_name((day_num(day) + days) % 7)


def days_in_month(month):
    if month in ["January", "March", "May", "July",
                 "August", "October", "December"]:
        return 31
    elif month == "February":
        return 28
    elif month in ["April", "June", "September",
                   "November"]:
        return 30
    return None


def to_secs(hours, minutes, seconds):
    return int((hours * 60 ** 2) + (minutes * 60) + seconds)


def hours_in(seconds):
    return int((seconds / 60) / 60)


def minutes_in(seconds):
    return int((seconds / 60) % 60)


def seconds_in(seconds):
    return seconds - hours_in(seconds) * 60 ** 2 - minutes_in(seconds) * 60


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    return -1


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def intercept(x1, y1, x2, y2):
    c = y1 - slope(x1, y1, x2, y2) * x1
    return slope(x1, y1, x2, y2) * x1 + c


def is_even(n):
    if n % 2 == 0:
        return True
    return False


def is_odd(n):
    if is_even(n):
        return False
    return True


def is_factor(f, n):
    if n % f == 0:
        return True
    return False

def is_multiple(f, n):
    if f % n == 0:
        return True
    return False


test_suite()
