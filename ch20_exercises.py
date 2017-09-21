from unit_tester import test

string = "ThiS is String with Upper and lower case Letters"


def number_of_letters_in_string(string):
    word = string.lower()

    tup = {}
    for letter in word:
        tup[letter] = tup.get(letter, 0) + 1

    lst = sorted(list(tup.items()))
    for (k, v) in lst:
        if k != " ":
            print(k, "\t", v)

# number_of_letters_in_string(string)


def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit, 0) + quantity


def test_suit():
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    test("strawberries" in new_inventory)
    test(new_inventory["strawberries"] == 10)

    add_fruit(new_inventory, "strawberries", 25)
    test(new_inventory["strawberries"] == 35)


#test_suit()


def myreplace(old, new, s):
    """
        Replace all occurrences of old with the new in s.
    """
    return new.join(s.split(old))


def clean_words(word):
    clean_word = ''
    for letter in word:
        if letter.isalpha():
            clean_word += letter
    lower_word = clean_word.lower()
    return lower_word


def has_dashdash(x):
    return x.find("--") != -1


def extract_words(x):
    clean_list = []
    if has_dashdash(x):
        x = myreplace("--", " ", x)
    words_punc = x.split()
    for word in words_punc:
        cleaned_word = clean_words(word).lower()
        clean_list.append(cleaned_word)
    return clean_list


def alices_words(book):
    """ Summaries the number of words in a book,
        and saves it to a text file."""
    infile = open(book, "r")
    outfile = open("alice_words.txt", "w")
    string_of_words = infile.read()
    #word_list = string_of_words.split()  # a different version of the same program
    word_list = extract_words(string_of_words)

    tup = {}
    for word in word_list:
        #new_word = clean_words(word.lower())  # a different version of the same program
        #tup[new_word] = tup.get(new_word, 0) + 1  # a different version of the same program
        tup[word] = tup.get(word, 0) + 1

    lst = sorted(list(tup.items()))
    for (k, v) in lst:
        if k != " ":
            outfile.write("{0:15s} : {1}\n".format(k, v))
    infile.close()
    outfile.close()

alices_words("alice_in_wonderland.txt")