from unit_tester import test


def test_suit():
    test(not share_diagonal(5, 2, 2, 0))
    test(share_diagonal(5, 2, 3, 0))
    test(share_diagonal(5, 2, 4, 3))
    test(share_diagonal(5, 2, 4, 1))

    test(not col_clashes([6, 4, 2, 0, 5], 4))
    test(not col_clashes([6, 4, 2, 0, 5, 7, 1, 3], 7))

    test(col_clashes([0, 1], 1))
    test(col_clashes([5, 6], 1))
    test(col_clashes([6, 5], 1))
    test(col_clashes([0, 6, 4, 3], 3))
    test(col_clashes([5, 0, 7], 2))
    test(not col_clashes([2, 0, 1, 3], 1))
    test(col_clashes([2, 0, 1, 3], 2))

    test(not has_clashes([6, 4, 2, 0, 5, 7, 1, 3]))
    test(has_clashes([4, 6, 2, 0, 5, 7, 1, 3]))
    test(has_clashes([0, 1, 2, 3]))
    test(not has_clashes([2, 0, 3, 1]))
    test(has_clashes([3, 2, 4, 0, 6, 1, 5, 7]))

    test(mirror_x_axis([6, 4, 2, 0, 5, 7, 1, 3]) == [1, 3, 5, 7, 2, 0, 6, 4])
    test(mirror_x_axis([1, 3, 0, 2]) == [2, 0, 3, 1])

    test(mirror_y_axis([6, 4, 2, 0, 5, 7, 1, 3]) == [3, 1, 7, 5, 0, 2, 4, 6])
    test(mirror_y_axis([1, 3, 0, 2]) == [2, 0, 3, 1])

    test(rotate_90_degrees([1, 3, 0, 2]) == [1, 3, 0, 2])
    test(rotate_90_degrees([6, 4, 2, 0, 5, 7, 1, 3]) == [4, 1, 5, 0, 6, 3, 7, 2])

    test(rotate_180_degrees([1, 3, 0, 2]) == [1, 3, 0, 2])
    test(rotate_180_degrees([6, 4, 2, 0, 5, 7, 1, 3]) == [4, 6, 0, 2, 7, 5, 3, 1])

    test(rotate_270_degrees([1, 3, 0, 2]) == [1, 3, 0, 2])
    test(rotate_270_degrees([6, 4, 2, 0, 5, 7, 1, 3]) == [5, 0, 4, 1, 7, 2, 6, 3])

    test(family_of_symmetries([0, 4, 7, 5, 2, 6, 1, 3]) ==
         [[0, 4, 7, 5, 2, 6, 1, 3], [7, 1, 3, 0, 6, 4, 2, 5],
          [4, 6, 1, 5, 2, 0, 3, 7], [2, 5, 3, 1, 7, 4, 6, 0],
          [3, 1, 6, 2, 5, 7, 4, 0], [0, 6, 4, 7, 1, 3, 5, 2],
          [7, 3, 0, 2, 5, 1, 6, 4], [5, 2, 4, 6, 0, 3, 1, 7]])


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y) on the same shared diagonal with (x1, y1)? """
    dx = abs(x1 - x0)  # Calc the absolute y distance
    dy = abs(y1 - y0)  # Calc the absolute x distance
    return dx == dy  # They clash if dx == yx


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
        with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False  # No clashes - col c has a safe placement


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonal.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def main(board_size):
    import random
    solutions = []  # A list of unique solutions
    rng = random.Random()  # Instantiate a generator

    bd = list(range(board_size))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd) and bd not in solutions:
            print("Found solution {0} in {1} tries.".format(bd, tries))
            solutions.append(list(bd))
            tries = 0
            num_found += 1
    for i in solutions:
        print(i)


def mirror_y_axis(bd):
    return bd[::-1]


def mirror_x_axis(bd):
    return [((len(bd)-1) - i) for i in bd]


def rotate_90_degrees(bd):
    """ Rotate the board anti-clockwise.
        The value becomes the index.
        The index becomes the value = (len(bd) - 1) - index)
    """
    a = []
    n = []
    for (i, j) in enumerate(bd):
        a.append([j, (len(bd) - 1) - i])
    a.sort()
    for x, y in a:
        n.append(y)
    return n


def rotate_180_degrees(bd):
    return rotate_90_degrees(rotate_90_degrees(bd))


def rotate_270_degrees(bd):
    x = rotate_180_degrees(bd)
    y = rotate_90_degrees(x)
    return y


def family_of_symmetries(bd):
    family = [bd, rotate_90_degrees(bd),
              rotate_180_degrees(bd), rotate_270_degrees(bd),
              mirror_y_axis(bd), rotate_270_degrees(mirror_x_axis(bd)),
              mirror_x_axis(bd), rotate_270_degrees(mirror_y_axis(bd))]
    return family


if __name__ == "__main__":
    test_suit()
    # main(8)
    # print(family_of_symmetries([0, 4, 7, 5, 2, 6, 1, 3]))
