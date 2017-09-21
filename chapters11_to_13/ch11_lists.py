def nested_loops():
    #Nested loops for Nested Data
    students = [("John", ["CompSci", "Physics"]),
                ("Vusi", ["Maths", "CompSci", "Stats"]),
                ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
                ("Sarah", ["InfSys", "Accounting", "Economics", "Management"]),
                ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
                ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])
                ]


    # Count how many students are taking CompSci
    counter = 0
    for (name, subjects) in students:
        if "CompSci" in subjects:
            counter += 1

    print("Then number of students taking CompSci is", counter)


def not_enumerate():
    xs = [1, 2, 3, 4, 5]
    for i in range(len(xs)):
        xs[i] **= 2
        print(xs[i])


def enumerate_example():
    xs = [1, 2, 3, 4, 5]

    for (i, val) in enumerate(xs):
        xs[i] = val ** 2
        print(xs[i])


def enumerate_words():
    for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
        print(i, v)


def double_stuff(a_list):
    """ Overwrite each element in a_list with double its value. """
    for (idx, val) in enumerate(a_list):
        a_list[idx] = 2 * val

def double_stuff_2(a_list):
    """ Return a new list which contains
        doubles of the elements in a_list.
    """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list

#things = [2, 5, 9]
#double_stuff(things)
#xs = double_stuff_2(things)
#print(things)
#print(xs)


songs = "The rain in Spain..."
wd = songs.split("ai")
print(wd)
we = "ooooo".join(wd)
print(we)


#nested_loops()
#not_enumerate()
#enumerate_example()
#enumerate_words()
