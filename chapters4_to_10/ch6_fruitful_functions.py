import math
import sys


def find_first_2_letter_words(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return ""


def distance(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx ** 2 + dy ** 2)


def is_divisible(x, y):
    """Testing if x is exactly divisible by y."""
    return x % y == 0


def absolute_value(x):
    if x < 0:
        return -x
    return x


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
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

# xs = ["This", "is", "a", "dead", "is", "do", "parrot"]
# print(find_first_2_letter_words(xs)
# print(find_first_2_letter_words(["I", 'like', 'cheese', "mice"]))
# print(distance(1, 2, 4, 6))
#print(is_divisible(4, 6))

test_suite()
