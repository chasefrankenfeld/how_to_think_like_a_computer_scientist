def reverse_lines(old_file, new_file):
    infile = open(old_file, "r")
    outfile = open(new_file, "w")
    text = infile.readlines()
    y = len(text) - 1
    while y != -1:
        outfile.write(text[y])
        y -= 1
    infile.close()
    outfile.close()


def print__lines_with_snake(file):
    infile = open(file, "r")
    for x in infile:
        if "snake" in x:
            print(x, end="")
    infile.close()


def add_numbers_to_file(old_file, new_file):
    infile = open(old_file, "r")
    outfile = open(new_file, "w")
    lines = infile.readlines()
    for (num, line) in enumerate(lines):
        outfile.write('%4d %s' % (num + 1, line))
    infile.close()
    outfile.close()


def remove_numbers_from_files(old_file, new_file):
    """
    The goal is to remove eveything thing from the front
    of each line that is not a string. This includes
    spaces, numbers, and all other non-alphanumeric characters.
    """
    infile = open(old_file, "r")
    outfile = open(new_file, "w")
    while True:
        text = infile.readline()
        if text[0] in "ABCDEGGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            continue
        outfile.write(text[1:])
    infile.close()
    outfile.close()


# reverse_lines("test.txt", "test_2.txt")
# print__lines_with_snake("test.txt")
# add_numbers_to_file("test.txt", "test_.txt")
#remove_numbers_from_files("test_2.txt", "test_3.txt")
