from unit_tester import test

xs1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
ys = [4, 8, 12, 16, 20, 24]
zs = xs1 + ys
zs.sort()


def test_suite():
    test(merge(xs1, []) == xs1)
    test(merge(ys, []) == ys)
    test(merge([], []) == [])
    test(merge(xs1, ys) == zs)
    test(merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5])
    test(merge(['a', 'big', 'cat'], ['big', 'bite', 'dog']) == ['a', 'big', 'big', 'bite', 'cat', 'dog'])

    test(merge_only_matching_items([1, 2, 3], [3, 4, 5]) == [3, 3])
    test(merge_only_matching_items(['a', 'big', 'cat'], ['big', 'bite', 'dog']) == ['big', 'big'])
    test(merge_only_matching_items([3, 4, 5], [1, 2, 3]) == [3, 3])

    test(merge_only_items_in_first_list([1, 2, 3], [3, 4, 5]) == [1, 2])
    test(merge_only_items_in_first_list(['a', 'big', 'cat'], ['big', 'bite', 'dog']) == ['a', 'cat'])
    test(merge_only_items_in_first_list([3, 4, 5], [1, 2, 3]) == [4, 5])

    test(merge_only_items_in_second_list([1, 2, 3], [3, 4, 5]) == [4, 5])
    test(merge_only_items_in_second_list(['a', 'big', 'cat'], ['big', 'bite', 'dog']) == ['bite', 'dog'])
    test(merge_only_items_in_second_list([3, 4, 5], [1, 2, 3]) == [1, 2])

    test(merge_not_repeated_items([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5])
    test(merge_not_repeated_items(['a', 'big', 'cat'], ['big', 'bite', 'dog']) == ['a', 'bite', 'cat', 'dog'])
    test(merge_not_repeated_items([3, 4, 5], [1, 2, 3]) == [1, 2, 4, 5])

    test(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])
    test(bagdiff([1, 2, 3, 3, 4], [3, 4, 5]) == [1, 2, 3])
    test(bagdiff(['a', 'big', 'cat'], ['a', 'big', 'bite', 'dog']) == ['cat'])
    test(bagdiff([3, 4, 5], [1, 2, 3]) == [4, 5])


def merge(xs, ys):
    """ Merge SORTED lists xs and ys.
        Return a sorted result.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            result.extend(ys[yi:])  # Add remaining items from ys
            return result  # And we're done

        if yi >= len(ys):  # Same as xi >= len(xs)
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def merge_only_matching_items(xs, ys):
    """ Merge SORTED lists xs and ys.
        Return only values in both lists.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            return result  # And we're done

        if yi >= len(ys):  # Same as xi >= len(xs)
            return result

        # Both lists still have items, copy matching items to result
        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            result.append(ys[yi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1


def merge_only_items_in_first_list(xs, ys):
    """ Merge SORTED lists xs and ys.
        Return only values in both lists.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            return result  # And we're done

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy item from only in first list to result
        if xs[xi] == ys[yi]:
            xi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1


def merge_only_items_in_second_list(xs, ys):
    """ Merge SORTED lists xs and ys.
        Return only values in both lists.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            result.extend(ys[yi:])
            return result  # And we're done

        if yi >= len(ys):
            return result

        # Both lists still have items, copy only items in second list to result
        if xs[xi] == ys[yi]:
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def merge_not_repeated_items(xs, ys):
    """ Merge SORTED lists xs and ys.
        Return only values in both lists.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            result.extend(ys[yi:])
            return result  # And we're done

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy only items in second list to result
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1



def bagdiff(xs, ys):
    """ Merge SORTED lists xs and ys.
        Return only values in both lists.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            return result  # And we're done

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy only items in second list to result
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1


test_suite()