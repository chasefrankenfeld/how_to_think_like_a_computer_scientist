from unit_tester import test


friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

def search_linear(list, name):
    for (i, v) in enumerate(list):
        if v == name:
            return i
    return -1
    # Version 2
    # x = 0
    # while x < len(list):
    #     if list[x] == name:
    #         return x
    #     x += 1
    # return -1

# test(search_linear(friends, "Zoe") == 1)
# test(search_linear(friends, "Joe") == 0)
# test(search_linear(friends, "Paris") == 6)
# test(search_linear(friends, "Bill") == -1)

vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()


def find_unknown_words(vocab, book_words):
    x = list()
    for word in book_words:
        if search_linear(vocab, word) < 0:
            x.append(word)
    return x

# test(find_unknown_words(vocab, book_words) == ["from", "to"])
# test(find_unknown_words([], book_words) == book_words)
# test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

def text_to_words(the_text):
    """ return a list of words with all punctuations removed """
    substitutions = the_text.maketrans(
    # If you find any of these
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
    # Replace them by these
    "abcdefghijklmnopqrstuvwxyz                                          "
    )
    return the_text.translate(substitutions).split()


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

# book_words = get_words_in_book("alice_in_wonderland.txt")
# print("There are {0} words in the book, the first 100 are\n{1}".
#                         format(len(book_words), book_words[:100]))


xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]

def search_binary(xs, target):
    """ Find and return the index of the key in the list """
    lower_index = 0
    upper_index = len(xs)
    while True:
        if lower_index == upper_index:  # if the region of interest becomes empty
            return -1
        # Probe the middle of the list
        middle_index = (upper_index + lower_index) // 2
        # Fetch the item
        item_at_middle = xs[middle_index]

        print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'".
                format(lower_index, upper_index,
                        upper_index - lower_index,
                        item_at_middle, target))

        # How does the probed item compare to the target?
        if item_at_middle == target:
            return middle_index  # Found it
        if item_at_middle < target:
            lower_index = middle_index + 1  # Use upper half of the region of interest next time
        else:
            upper_index = middle_index  # Use the lower half of the region of interest next time


# test(search_binary(xs, 20) == -1)
# test(search_binary(xs, 99) == -1)
# test(search_binary(xs, 1) == -1)
# for (i, v) in enumerate(xs):
#     test(search_binary(xs, v) == i)

def remove_adjacent_dups(a_list):
    """ Return a new list in which all adjacent duplicates
        from a sorted list have been removed
    """
    result = []
    most_recent_elem = None
    for e in a_list:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result

# test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
# test(remove_adjacent_dups([]) == [])
# test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
#                                         ["a", "big", "bite", "dog"])


# all_words = get_words_in_book("alice_in_wonderland.txt")
# all_words.sort()
# book_words = remove_adjacent_dups(all_words)
# print("There are {0} words in the book. Only {1} are unique.".
#                         format(len(all_words), len(book_words)))
# print("The first 100 words are\n{0}".format(book_words[:100]))

def merge(xs, ys):
    """ Merge sorted lists xs & ys, and return the list """
    result = []
    xi = 0
    yi = 0

    while True:

        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
qs = [3,4,9,12,17]
zs = xs+ys
zs.sort()
bs = []
cs = [3,9,17]
ds = [1,3,5,7,9,11,13,15,17,19]
es = [1,5,7,11,13,15,19]

# test(merge(xs, []) == xs)
# test(merge([], ys) == ys)
# test(merge([], []) == [])
# test(merge(xs, ys) == zs)
# test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
# test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
#                                 ["a", "big", "big", "bite", "cat", "dog"])

def items_present_in_both(xs, ys):
    """ Return only elements present in both lists """
    result = []
    xi = 0
    yi = 0

    while True:

        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            yi += 1
            xi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1

def items_present_in_first_by_not_second_list(xs, ys):
    """ when comparing two lists, return elements only present in the first lists """
    result = []
    for item in xs:
        if item not in ys:
            result.append(item)
    return result

def items_present_in_second_but_not_first_list(xs, ys):
    """ when comparing two lists, return elements only present in the second lists """
    # result = []
    # for item in ys:
    #     if item not in xs:
    #         result.append(item)
    # return result
    result = []
    xi = 0
    yi = 0
    while True:

        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:
            yi += 1
        elif xs[xi] < ys[xi]:
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def return_all_items_of_both_list_no_duplicates(xs, ys):
    merged_list = merge(xs, ys)
    return remove_adjacent_duplicates(merged_list)

def bagdiff(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1






test(items_present_in_both(xs, ys) == bs)
test(items_present_in_both(xs, qs) == cs)
test(items_present_in_first_by_not_second_list(xs, ys) == ds)
test(items_present_in_first_by_not_second_list(xs, qs) == es)
test(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])
