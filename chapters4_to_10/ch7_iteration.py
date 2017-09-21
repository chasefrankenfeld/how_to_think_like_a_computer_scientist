import sys
import random


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
    test(mysum([1, 2, 3, 4]) == 10)

    test(sum_to(4) == 10)
    test(sum_to(1000) == 500500)

    test(num_digits(710) == 3)

    test(num_zero_and_five_digits(1055030250) == 7)
    test(num_zero_and_five_digits(0) == 1)


def mysum(xs):
    """Summing all the numbers in a list."""
    total = 0
    for x in xs:
        total += x
    return total


def sum_to(n):
    """Return the sum of 1+2+3 .... n"""
    ss = 0
    v = 1
    while v <= n:
        ss += v
        v += 1
    return ss


def seq3np1(n):
    """Print the 3n + 1 sequence from n,
       terminating when it reaches 1.
    """
    count = 0
    while n != 1:
        print(n, end=", ")
        count += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    print(n, end='.\n')
    print(count)


def num_digits(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count += 1
        n //= 10
    return count


#for x in range(13):
#    print(x, "\t", 2 ** x)


def print_multiples(n, high):
    for i in range(1, high + 1):
        print(n * i, end="\t")
    print()


def print_mult_table(high):
    for i in range(1, high + 1):
        print_multiples(i, i + 1)


#for i in [12, 16, 17, 24, 29]:
#    if i % 2 == 1:  # If the number is odd
#        break  # ... Immediately exit the loop
#    print(i)
#print("done")


#total = 0
#while True:
#    response = input("Enter the next number. (Leave blank to end)" )
#    if response == "":
#        break
#    total += int(response)
#print("The total of the numbers you entered is ", total)

def game():
    rng = random.Random()
    number = rng.randrange(1, 1000)

    guesses = 0
    msg = ""

    while True:
        guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
        guesses += 1
        if guess > number:
            msg += str(guess) + " is too high.\n"
        elif guess < number:
            msg += str(guess) + " is too low.\n"
        else:
            break

    input("\n\nGreat, you got it in {} guesses!!\n\n".format(guesses))


#for i in [12, 16, 17, 24, 29]:
#    if i % 2 == 1:  # If the number is odd
#        continue  # ... Don't process it
#    print(i)
#print("done")


def tuples():
    celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1973), ("Justin Bieber", 1994)]
    print(celebs)
    print(len(celebs))

    for (name, year) in celebs:
        if year < 1970:
            print(name)

students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])
]

# Print all students with a count of their courses
for (name, subjects) in students:
    print(name, "takes", len(subjects), "courses")
print("")

counter = 0
for (name, subjects) in students:
    for s in subjects:
        if s == "CompSci":
            counter += 1
print("The number of students taking CompSci is", counter)


def sqrt(n):
    approx = n/2.0  #Start with some or other guess at the answer
    while True:
        better = (approx + n/approx) / 2.0
        if abs(approx - better) < 0.00001:
            return better
        approx = better

#Test these cases
print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))

#test_suite()
