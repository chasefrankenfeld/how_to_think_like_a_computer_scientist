import random
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
    test(odd_numbers([1, 2, 3, 4, 5, 6, 7]) == 4)

    test(sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]) == 20)

    test(sum_of_negative_numbers([-1, -2, -3, 5, 3, -1]) == -7)
    test(sum_of_negative_numbers([-1, -2, -3, 5, 3, -4]) == -10)

    test(word_length_is_5(['hello', 'I', 'am', 'Chase']) == 2)
    test(word_length_is_5(['chase', 'chase', 'cars', 'hello']) == 3)

    test(num_of_odd_numbers_up_to_even_number([3, 3, 5, 7, 6]) == 4)
    test(num_of_odd_numbers_up_to_even_number([1, 2, 3, 4, 7, 9]) == 1)
    test(num_of_odd_numbers_up_to_even_number([1, -3, 5, 7, 9]) == 5)

    test(number_of_words_up_to_sam(['i', 'list', 'grrr', 'sam']) == 3)
    test(number_of_words_up_to_sam(['i', 'list', 'sam', 'grrr']) == 2)
    test(number_of_words_up_to_sam(['i', 'list', 'grrr']) == 3)
    test(number_of_words_up_to_sam(['sam', 'i', 'list', 'sam', 'grrr']) == 0)

    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(11071991))

    test(num_digits(0) == 1)
    test(num_digits(710) == 3)
    test(num_digits(12345) == 5)
    test(num_digits(-12345) == 5)

    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)

    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


def odd_numbers(lst):
    count = 0
    for i in lst:
        if i % 2 == 1:
            count += 1
    return count


def sum_of_even_numbers(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += i
    return count


def sum_of_negative_numbers(lst):
    count = 0
    for i in lst:
        if i < 0:
            count += i
    return count


def word_length_is_5(lst):
    count = 0
    for i in lst:
        if len(i) == 5:
            count += 1
    return count


def num_of_odd_numbers_up_to_even_number(lst):
    count = 0
    for i in lst:
        if i % 2 == 1:
            count += 1
        else:
            break
    return count


def number_of_words_up_to_sam(lst):
    count = 0
    for i in lst:
        if i == 'sam':
            break
        else:
            count += 1
    return count


def sqr(n):
    approx = n / 2.0
    while True:
        better = (approx + n / approx) / 2.0
        if abs(approx - better) == 0.01:
            return better
        approx = better


def print_multiples(n, high):
    for i in range(1, high + 1):
        print(n * i, end="\t")
    print()


def print_mult_table(high):
    for i in range(1, high + 1):
        print_multiples(i, i + 1)


def print_triangular_numbers(n):
    for i in range(1, n + 1):
        dots = (i * (i + 1)) / 2
        print(i, "\t", int(dots))


def is_prime(n):
    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n % 4 == 0:
        return False
    elif n % 5 == 0:
        return False
    elif n % 7 == 0:
        return False
    else:
        return True


def num_digits(x):
    x = abs(x)
    count = 0
    if x == 0:
        count += 1
    while x != 0:
        count += 1
        x //= 10
    return count


def num_even_digits(x):
    count = 0
    if x == 0:
        count += 1
    while x != 0:
        if x % 2 == 0:
            count += 1
        x //= 10
    return count


def sum_of_squares(xs):
    count = 0
    for x in xs:
        count += x**2
    return count


def play_once(human_plays_first):
    """"
        Must play one round of the game. If the parameter is True,
        the human gets to play first, else the computer gets to play first.
        When the round ends, the return value of the function is one of
        -1 (human wins), 0 (game drawn), 1 (computer wins).
    """

    # THis is all dummy scaffolding code right at the moment
    rng = random.Random()

    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first = {0}, winner = {1}".format(human_plays_first, result))

    return result


def the_game():
    computer_wins = 0
    player_wins = 0
    game_draws = 0
    total_games = computer_wins + player_wins + game_draws
    #percentage_of_wins = (player_wins / total_games) * 100
    while True:
        play = input("Do you want to play?" )
        if play.lower() == "y":
            human_plays_first = input("Select a random number between -1 and 1:" )
            who_wins = play_once(human_plays_first)
            if who_wins == 0:
                print("Game Drawn")
                game_draws += 1
            elif who_wins == 1:
                print("Computer Wins")
                computer_wins += 1
            else:
                print("You Win")
                player_wins += 1
            print("Player Wins: {}, Computer Wins: {}, Draws: {}".format(player_wins, computer_wins, game_draws))
            #print("You won {}% of the games player".format(percentage_of_wins))
        else:
            print("Goodbye!")
            break


#test_suite()
# print(print_mult_table(10))
# print(print_multiples(10, 10))
# print_triangular_numbers(5)

the_game()