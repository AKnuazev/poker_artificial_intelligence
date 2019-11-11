import string
import math
import random
import PyQt5

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["♠", "♣", "♥", "♦"]  # "spades", " clubs", "hearts", "diamonds"
players_number = 2


def check_royal_flush(hand):
    sorted_hand = sorted(hand)
    current_value = 10  # 10 value
    current_suit = hand[0].cards[0].suit
    in_a_row_counter = 0

    for card in sorted_hand:
        if card.suit == current_suit and card.value == current_value:
            current_value += 1
            in_a_row_counter += 1
        else:
            current_suit = card.suit
            current_value = card.value
            in_a_row_counter = 0

    if in_a_row_counter > 4:
        print('Royal Flush')
        return 1

    return 0


def check_straight_flush(hand):
    sorted_hand = sorted(hand)

    current_value = hand[0].cards[0].value
    current_suit = hand[0].cards[0].suit
    in_a_row_counter = 0

    for card in sorted_hand:
        if card.suit == current_suit and card.value == current_value:
            current_value += 1
            in_a_row_counter += 1
        else:
            current_suit = card.suit
            current_value = card.value
            in_a_row_counter = 0

    if in_a_row_counter > 4:
        print('Straight Flush')
        return 1

    return 0


def check_four(hand):
    sorted_hand = sorted(hand)

    current_value = hand[0].cards[0].value
    current_suit = hand[0].cards[0].suit
    same_cards_counter = 0

    for card in sorted_hand:
        if card.value == current_value:
            current_value += 1
            same_cards_counter += 1
        else:
            current_value = card.value
            same_cards_counter = 0

    if same_cards_counter == 4:
        print('Four of a kind')
        return 1

    return 0


def check_full_house(hand):
    sorted_hand = sorted(hand)

    current_value = hand[0].cards[0].value
    current_suit = hand[0].cards[0].suit
    same_cards_counter = 0

    for card in sorted_hand:
        if card.value == current_value:
            current_value += 1
            same_cards_counter += 1
        else:
            current_value = card.value
            same_cards_counter = 0

        if same_cards_counter == 3:
            for i in range(2):
                sorted_hand.remove(card)

    if same_cards_counter == 4:
        print('Four of a kind')
        return 1

    return 0


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        if self.value == 14:
            value = 'A'
        elif self.value == 13:
            value = 'K'
        elif self.value == 12:
            value = 'Q'
        elif self.value == 11:
            value = 'J'
        else:
            value = self.value
        return str(value) + self.suit

    def __eq__(self, second):
        return self.value == second.value

    def __ne__(self, second):
        return self.value != second.value

    def __lt__(self, second):
        return self.value < second.value

    def __le__(self, second):
        return self.value <= second.value

    def __gt__(self, second):
        return self.value > second.value

    def __ge__(self, second):
        return self.value >= second.value


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(value, suit)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop()

    def __len__(self):
        return len(self.deck)


class Hand:
    cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    def check_combination(self, board):
        comb_power = 0
        kicker_power = 0

    def __eq__(self, second):
        return self.value == second.value

    def __ne__(self, second):
        return self.value != second.value

    def __lt__(self, second):
        return self.value < second.value

    def __le__(self, second):
        return self.value <= second.value

    def __gt__(self, second):
        return self.value > second.value

    def __ge__(self, second):
        return self.value >= second.value


class Table(object):
    def __init__(self, num_hands):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = []
        self.tlist = []  # create a list to store total_point
        numCards_in_Hand = 5

        for i in range(num_hands):
            hand = Hand()
            for j in range(numCards_in_Hand):
                hand.append(self.deck.deal())
            self.hands.append(hand)

    def play(self):
        for i in range(len(self.hands)):
            sortedHand = sorted(self.hands[i], reverse=True)
            hand = ''
            for card in sortedHand:
                hand = hand + str(card) + ' '
            print('Hand ' + str(i + 1) + ': ' + hand)

    def point(self, hand):  # point()function to calculate partial score
        sortedHand = sorted(hand, reverse=True)
        c_sum = 0
        valuelist = []
        for card in sortedHand:
            valuelist.append(card.value)
        c_sum = valuelist[0] * 13 ** 4 + valuelist[1] * 13 ** 3 + valuelist[2] * 13 ** 2 + valuelist[3] * 13 + \
                valuelist[4]
        return c_sum


deck = Deck()
deck.__init__()
deck.shuffle()
hand = Hand()
hand.__init__()
for i in range(7):
    hand.add_card(Deck.get_card())
