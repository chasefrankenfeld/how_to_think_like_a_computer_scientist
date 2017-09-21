import string

import sys


def test(did_pass):
    """Print the results of the test."""
    linenum = sys._getframe(1).f_lineno  # get the callers line num
    if did_pass:
        msg = "Test at line {} is ok.".format(linenum)
    else:
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)


def test_suite():
    """Run the suite of tests for code in this module (this file)."""
    test(reverse_string("happy") == "yppah")
    test(reverse_string("Python") == "nohtyP")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")

    test(mirror("happy") == "happyyppah")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")

    test(remove_letter("apple", "a") == "pple")
    test(remove_letter("banana", "a") == "bnn")
    test(remove_letter("banana", "z") == "banana")
    test(remove_letter("Mississippi", "i") == "Msssspp")
    test(remove_letter("", "b") == "")
    test(remove_letter("c", "b") == "c")

    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))

    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)

    test(remove("an", "banana") == "bana")
    test(remove("eggs", "bicycle") == "bicycle")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")

    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("eggs", "bicycle") == "bicycle")
    test(remove_all("iss", "Mississippi") == "Mippi")


def exercise_2():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter in "OQ":
            suffix = "uack"
        else:
            suffix = "ack"
        print(letter + suffix)


def find_example(word, letter, start=0, end=None):
    ix = start
    if end is None:
        end = len(word)
    while ix < end:
        if word(ix) == letter:
            return ix
    return -1


def count_letters(word, letter, start=0):
    """Exercise 3, then 4"""
    count = 0
    x = word.find(letter, start)
    while x != -1:
        count += 1
        x = word.find(letter, x + 1)
    return count


i_have_a_dream = """
Five score years ago, a great American, in whose symbolic shadow we
stand today, signed the Emancipation Proclamation. This momentous
decree came as a great beacon light of hope to millions of Negro slaves who
had been seared in the flames of withering injustice. It came as a joyous
daybreak to end the long night of their captivity."""


def removes_punctuation(story):
    string_without_punctuation = ""
    for letter in story:
        if letter not in string.punctuation:
            string_without_punctuation += letter
    return string_without_punctuation


def count_of_words_with_letters(story, letter, start=0):
    word_count = 0
    word_list = removes_punctuation(story).split()
    for word in word_list:
        if count_letters(word, letter, start) > 0:
            word_count += 1
    return word_count


def story_analysis(story, letter):
    number_of_words_in_story = len(removes_punctuation(story).split())
    number_of_words_containing_letter = count_of_words_with_letters(story, letter)
    percentage_of_words_with_letters = ((number_of_words_containing_letter / number_of_words_in_story) * 100)
    return 'Your text contains {0} words, of which {1} ({2:.1f}%) contain an "e".'.format(number_of_words_in_story,
                                                                                          number_of_words_containing_letter,
                                                                                          percentage_of_words_with_letters)


def print_multiples(num):
    for x in range(num + 1):
        print(int(num * x), end="   ")
    print()


def print_muti_tables(num):
    layout = "{0:>4}, {1:>4}, {2:>4}, {3:>4}, {4:>4}, {5:>4},{6:>4}, {7:>4}, {8:>4}, {9:>4}, {10:>4}, {11:>4}"
    for i in range(1, num + 1):
        str(print_multiples(i))


def print_multi_table_2(n):
    for row in range(1, n + 1):
        print(*("{:<3}".format(row * col) for col in range(1, n + 1)))


def reverse_string(x):
    return x[::-1]


def mirror(x):
    return x + reverse_string(x)


def remove_letter(word, letter):
    s = ''
    for i in word:
        if i not in letter:
            s += i
    return s


def is_palindrome(x):
    return x == reverse_string(x)


def count(sub, word):
    x = 0
    y = word.find(sub)
    while y != -1:
        x += 1
        y = word.find(sub, y + 1)
    return x


def remove(sub, word):
    y = word.find(sub)
    x = len(sub)
    if y != -1:
        in1 = word[:y]
        in2 = word[x + y:]
        return in1 + in2
    return word


def remove_all(sub, word):
    y = word.find(sub)
    while y != -1:
        s = remove(sub, word)
    return s


# exercise_2()
# print(count_letters("banana", "a"))
# print(removes_punctuation(i_have_a_dream))
# print(count_of_words_with_letters(i_have_a_dream, "e"))
# print(story_analysis(i_have_a_dream, "e"))
# multiplication_tables(6)
# print_multi_table_2(12)
# print(reverse_string("happy"))

test_suite()