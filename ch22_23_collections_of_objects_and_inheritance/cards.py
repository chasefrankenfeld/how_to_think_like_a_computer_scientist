class Card:

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
                        "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same, then check ranks
        if self.rank > other.rank:
            if other.rank == 1: return -1  # If the other card is an Ace (make the Ace the highest card)
            return 1
        if self.rank < other.rank:
            if self.rank == 1: return 1  # If self.card is an Ace (Make Ace the highest ranking card)
            return -1
        # Ranks are the same, then it's a tie
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        """ Highlighted code modifies the card list by swapping a selected card with a random card """
        import random
        rng = random.Random()  # Create a random generator
        # num_cards = len(self.cards)
        # for i in range(num_cards):
        #     j = rng.randrange(i, num_cards)  # Chooses a random integer i <= random card < num_cards
        #     (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def pop(self):
        """ To deal a card (last card in the deck - really bottom up) """
        return self.cards.pop()

    def is_empty(self):
        """ True if the deck is empty """
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break                    # Break if out of cards
            card = self.pop()            # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)               # Add the card to the hand


class Hand(Deck):

    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

    # Add a new card to the Hand (note: remove is inherited from Deck)
    def add(self, card):
        self.cards.append(card)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:  # since self.cards is modified in the loop, we don't want to use it in the loop
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}".
                        format(self.name, card, match))
                count += 1
        return count


class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()  ##############################

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play beigns")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0  # Keeps track of which players turn it is
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("----------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbour = self.find_neighbour(i)
        picked_card = self.hands[neighbour].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbour(self, i):
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbour = (i + next) % num_hands
            if not self.hands[neighbour].is_empty():
                return neighbour

    def print_hands(self):
        for hand in self.hands:
            print(hand)
