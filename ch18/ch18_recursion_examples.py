import os

import sys

from unit_tester import test


def test_suite():
    test(r_max([2, 9, [1, 13], 8, 6]) == 13)
    test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
    test(r_max(["joe", ["sam", "ben"]]) == "sam")

    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

    test(count(2, []) == 0)
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(count("a", [["this", ["a", ["thing", "a"], "a"], "is"], ["a", "easy"]]) == 4)

    test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]) == [2, 9, 2, 1, 13, 2, 8, 2, 6])
    test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6])
    test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6])
    test(flatten([["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]]) ==
         ["this", "a", "thing", "a", "is", "a", "easy"])
    test(flatten([]) == [])



def r_max(nxs):
    """
    Find the maximum in a recursive structure of lists
    within other ists.
    Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest


def recursive_min(lst):
    """
    Find the smallest nested number in a nested list.
    Precondition: There are no empty lists or sublists.
    """
    smallest = None
    first_time = True
    for i in lst:
        if type(i) == type([]):
            val = recursive_min(i)
        else:
            val = i

        if first_time or val < smallest:
            first_time = False
            smallest = val

    return smallest


def count(target, lst):
    """ Count the amount of times, a number is in a list and nested list """
    n = 0
    for i in lst:
        if type(i) == type([]):
            n += count(target, i)
        elif i == target:
            n += 1
    return n


def flatten(lst):
    """ Return a list of all values in a nested list """
    flatten_list = []
    for i in lst:
        if type(i) == type([]):
            flatten_list += flatten(i)
        else:
            flatten_list.append(i)

    return flatten_list


def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


def fib_1(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number+1)




if __name__ == '__main__':
    sys.getrecursionlimit()
    recursion_depth(0)





#test_suite()


