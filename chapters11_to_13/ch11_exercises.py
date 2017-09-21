import sys


def test(did_pass):
    """ Print the rests of the test """
    linenum = sys._getframe(1).f_lineno  # gets the callers line number
    if did_pass:
        msg = "Test at line {} is ok.".format(linenum)
    else:
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)


def test_suit():
    """ Run the suite of tests for the code in this module (this file). """
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

    test(cross_product([2, 3, 4], [5, 6, 7]) == [-3, 6, -3])
    test(cross_product([3, -3, 1], [4, 9, 2]) == [-15, -2, 39])
    test(cross_product([3, -3, 1], [-12, 12, -4]) == [0, 0, 0])

    test(cross_product_1([2, 3, 4], [5, 6, 7]) == [-3, 6, -3])
    test(cross_product_1([3, -3, 1], [4, 9, 2]) == [-15, -2, 39])
    test(cross_product_1([3, -3, 1], [-12, 12, -4]) == [0, 0, 0])

    s = "I love spom! Spom is my favourite food. Spom, spom, yum"
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    test(replace(s, "om", "am") == "I love spam! Spam is my favourite food. Spam, spam, yum")
    test(replace(s, "o", "a") == "I lave spam! Spam is my favaurite faad. Spam, spam, yum")


def add_vectors(u, v):
    lst = []
    for (i, j) in enumerate(u):
        lst += [v[i] + u[i]]
    return lst


def scalar_mult(s, v):
    lst = []
    for i in v:
        lst.append(s * i)
    return lst


def dot_product(u, v):
    count = 0
    answer = 0
    lst = []
    for (i, j) in enumerate(u):
        lst += [v[i] * u[i]]
    while len(lst) > count:
        answer += lst[count]
        count += 1
    return answer


def cross_product(u, v):
    lst = []
    for a in range(len(u)):
        if a == 0:
            j, k = 1, 2
            lst += [u[j] * v[k] - u[k] * v[j]]
        elif a == 1:
            j, k = 2, 0
            lst += [u[j] * v[k] - u[k] * v[j]]
        else:
            j, k = 0, 1
            lst += [u[j] * v[k] - u[k] * v[j]]
    return lst


def cross_product_1(u, v):
    lst = []
    lst += [u[1] * v[2] - u[2] * v[1]]
    lst += [u[2] * v[0] - u[0] * v[2]]
    lst += [u[0] * v[1] - u[1] * v[0]]
    return lst


song = "The rain in spain..."


def word_play(w):
    return " ".join(w.split())


def replace(s, old, new):
    s_without_old = s.split(old)
    s_with_new = new.join(s_without_old)
    return s_with_new


def swap(x, y):     # Incorrect versions
    print("before swap statement: x", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x", x, "y:", y)

a = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a", a, "b:", b)
swap(a, b)
print("after swap function call: a", a, "b:", b)


#test_suit()
#print(word_play(song))
