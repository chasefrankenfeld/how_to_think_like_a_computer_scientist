from unit_tester import test

import time

friends = ["Joe", "Zoe", "Brad", "Angeline", "Ziku", "Thandi", "Paris"]

vocab = ['apple', 'boy', 'dog', 'down', 'fell', 'girl', 'grass', 'the', 'tree']
book_words_1 = "the apple fell from the tree to the grass".split()

xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]

xs1 = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs1 + ys
zs.sort()


def test_suite():
    test(search_linear(friends, "Zoe") == 1)
    test(search_linear(friends, "Joe") == 0)
    test(search_linear(friends, "Paris") == 6)
    test(search_linear(friends, "Bill") == -1)

    test(find_unknown_words(vocab, book_words_1) == ["from", "to"])
    test(find_unknown_words([], book_words_1) == book_words_1)
    test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

    test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
    test(text_to_words('"Well, I never!", said Alice.') == ["well", "i", "never", "said", 'alice'])

    test(search_binary(xs, 20) == -1)
    test(search_binary(xs, 99) == -1)
    test(search_binary(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        test(search_binary(xs, v) == i)

    test(remove_adjacent_duplicates([1, 2, 3, 3, 3, 3, 5, 6, 9, 9]) == [1, 2, 3, 5, 6, 9])
    test(remove_adjacent_duplicates([]) == [])
    test(remove_adjacent_duplicates(['a', 'big', 'big', 'bite', 'dog']) == ['a', 'big', 'bite', 'dog'])

    test(merge(xs1, []) == xs1)
    test(merge(ys, []) == ys)
    test(merge([], []) == [])
    test(merge(xs1, ys) == zs)
    test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
    test(merge(['a', 'big', 'cat'], ['big', 'bite', 'dog']) == ['a', 'big', 'big', 'bite', 'cat', 'dog'])


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs"""
    for (i, val) in enumerate(xs):
        if val == target:
            return i
    return -1


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0  # Lower bound
    ub = len(xs)  # Upper bound
    while True:
        if lb == ub:  # If region of interest (ROI) become empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        #print("ROI[{0}:{1}](size = {2}), probed='{3}', target='{4}'"
        #     .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index  # Found it
        if item_at_mid < target:
            lb = mid_index + 1  # Use upper half of ROI next time
        else:
            ub = mid_index  # Use lower half of ROI next time


def find_unknown_words(vocab, wds):
    """ Return a list of words in the wds that do not occur in vocab. """
    result = []
    for item in wds:
        if search_binary(vocab, item) < 0:
            result.append(item)
    return result


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


def text_to_words(the_text):
    """
    Return a list of words with all punctuations removed,
    and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


def remove_adjacent_duplicates(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result


def merge(xs, ys):
    """ Merge SORTED lists xs and ys.
        Return a sorted result.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):           # If xs list is finished
            result.extend(ys[yi:])  # Add remaining items from ys
            return result           # And we're done

        if yi >= len(ys):           # Same as xi >= len(xs)
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
        list of words from wds that do not occur in vocab.
    """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(vocab):  # If xs list is finished
            result.extend(wds[yi:])
            return result  # And we're done

        if yi >= len(wds):
            return result

        # Both lists still have items, copy only items in second list to result
        if vocab[xi] == wds[yi]:
            yi += 1
        elif vocab[xi] < wds[yi]:
            xi += 1
        else:
            result.append(wds[yi])
            yi += 1



bigger_vocab = load_words_from_file("vocab.txt")
#print("There are {0} words in the vocab, starting with:\n {1}"
#      .format(len(bigger_vocab), bigger_vocab[0:6]))

#book_words = get_words_in_book("alice_in_wonderland.txt")
#print("There are {0} words in the book, the first 100 are\n{1}".
#      format(len(book_words), book_words[:100]))

#t0 = time.clock()
#missing_words = find_unknown_words(bigger_vocab, book_words)
#print(missing_words)
#t1 = time.clock()
#print("There are {0} unknown words.".format(len(missing_words)))
#print("That clock took {0:4f} seconds.".format(t1-t0))

all_words = get_words_in_book("alice_in_wonderland.txt")
t0 = time.clock()
all_words.sort()
book_words_2 = remove_adjacent_duplicates(all_words)
missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words_2)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))


test_suite()
