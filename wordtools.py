from unit_tester import test


def test_suite():
    test(myreplace(",", ";", "this, that, and some other thing") ==
         "this; that; and some other thing")
    test(myreplace(" ", "**", "Words will now be separated by stars.") ==
         "Words**will**now**be**separated**by**stars.")

    test(cleanwords("what?") == "what")
    test(cleanwords("'now!'") == "now")
    test(cleanwords("?+='w-o-r-d!,@$()'") == "word")

    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("dist--ance--but"))
    test(not has_dashdash("-yo-yo-"))

    test(extract_words("Now is the time! 'Now', is the time? Yes, now") ==
         ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
         ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])

    test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is", ["now", "is", "time", "is", "now", "is", "is"]) == 4)
    test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
         ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wordset(["or", "a", 'am', 'is', "are", 'be', 'be', 'but', 'am']) ==
         ['a', 'am', 'are', 'be', 'but', 'is', 'or'])

    test(longestword(['a', 'apple', 'pear', 'grape']) == 5)
    test(longestword(['a', 'am', 'I', 'be']) == 2)
    test(longestword(['this', 'supercalifragilisticexpialidocious']) == 34)
    test(longestword([]) == 0)


def myreplace(old, new, s):
    """
        Replace all occurrences of old with the new in s.
    """
    return new.join(s.split(old))


def cleanwords(x):
    l = ""
    for i in x:
        if i.isalpha():
            l += i
    return l


def has_dashdash(x):
    return x.find("--") != -1


def extract_words(x):
    clean_list = []
    if has_dashdash(x):
        x = myreplace("--", " ", x)
    words_punc = x.split()
    for word in words_punc:
        cleaned_word = cleanwords(word).lower()
        clean_list.append(cleaned_word)
    return clean_list


def wordcount(x, y):
    count = 0
    for i in y:
        if i == x:
            count += 1
    return count


def wordset(x):
    new_word_set = []
    for word in x:
        if word not in new_word_set:
            new_word_set += [word]
    return sorted(new_word_set)


def longestword(x):
    longest = ''
    for word in x:
        if len(word) > len(longest):
            longest = word
    return len(longest)


test_suite()