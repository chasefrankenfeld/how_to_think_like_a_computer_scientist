import random

from unit_tester import test

rnd = random.Random()

my_tickets = [
    [7, 17, 37, 19, 23, 43],
    [7, 2, 13, 41, 31, 43],
    [2, 5, 7, 11, 13, 17],
    [13, 17, 37, 19, 23, 43]
]


def test_suite():
    test(lotto_match([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]) == 3)

    test(lotto_matches([42, 4, 7, 11, 1, 13], my_tickets) == [1, 2, 3, 1])

    test(prime_in([42, 4, 7, 11, 1, 13]) == 3)

    test(prime_misses(my_tickets) == [3, 29, 47])


def lotto_ball():
    x = []
    for i in range(6):
        x.append(rnd.randrange(1, 49))
    return x


def lotto_match(ticket, draw):
    correct = 0
    for i in ticket:
        if i in draw:
            correct += 1
    return correct


def lotto_matches(draw, tickets):
    matches = []
    for ticket in tickets:
        matches.append(lotto_match(ticket, draw))
    return matches


def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif n == 1:
        return False
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n % 5 == 0:
        return False
    elif n % 7 == 0:
        return False
    else:
        return True


def prime_in(x):
    count = 0
    for i in x:
        if is_prime(i):
            count += 1
    return count


def prime_misses(my_tickets):
    prime = []
    my_ticket_numbers = []
    misses = []
    for i in range(50):
        if is_prime(i):
            prime.append(i)
    # print(prime)
    for x in my_tickets:
        for z in x:
            if z not in my_ticket_numbers:
                my_ticket_numbers.append(z)
    # print(sorted(my_ticket_numbers))
    for y in prime:
        if y not in my_ticket_numbers:
            misses.append(y)
    # print(misses)
    return misses


def main_lottory_draw(my_tickets):
    count = 0
    tickets_with_3 = 0
    while tickets_with_3 < 1:
        x = lotto_ball()
        count += 1
        y = lotto_matches(x, my_tickets)
        for i in y:
            if i >= 3:
                tickets_with_3 += 1
    return count


def average_lottory_draw():
    count = 0
    while count <= 20:
        main_lottory_draw(my_tickets)
        count += 1
        break



# test_suite()
