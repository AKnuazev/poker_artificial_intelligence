import random

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["♠", "♣", "♥", "♦"]  # "spades", " clubs", "hearts", "diamonds"
players_number = 2
combinations = {15: "Pair", 16: "Two pairs", 17: "Three of a kind", 18: "Straight", 19: "Flush", 20: "Full house",
                21: "Four of a kind", 22: "Straight flush", 23: "Royal flush"}
actions = {0: "Pass", 1: "Call", 2: "Raise"}

## Checks royal flush combination
def check_royal_flush(hand):
    sorted_hand = sorted(hand.cards)
    current_value = 10  # 10 value
    current_suit = sorted_hand[0].suit
    in_a_row_counter = 0

    for card in sorted_hand:
        if card.suit == current_suit and card.value == current_value:
            current_value += 1
            in_a_row_counter += 1
        elif card.value == current_value - 1:
            continue
        else:
            current_suit = card.suit
            in_a_row_counter = 1

    if in_a_row_counter > 4:
        # print('Royal Flush')
        return 1

    return 0

## Checks straight combination
def check_straight_flush(hand):
    sorted_hand = sorted(hand.cards)

    current_value = sorted_hand[0].value
    current_suit = sorted_hand[0].suit
    in_a_row_counter = 0

    for card in sorted_hand:
        if card.suit == current_suit and card.value == current_value:
            current_value += 1
            in_a_row_counter += 1
        elif card.value == current_value - 1:
            continue
        else:
            current_suit = card.suit
            current_value = card.value
            in_a_row_counter = 1

    if in_a_row_counter > 4:
        # print('Straight Flush')
        return 1

    return 0

## Checks four of a kind combination
def check_four_of_a_kind(hand):
    sorted_hand = sorted(hand.cards)

    current_card = sorted_hand[0]
    same_value_cards_counter = 0

    for card in sorted_hand:
        if card == current_card:
            same_value_cards_counter += 1
        else:
            current_card = card
            same_value_cards_counter = 1

    if same_value_cards_counter > 3:
        # print('Four of a kind')
        return 1

    return 0

## Checks full house combination
def check_full_house(hand):
    sorted_hand = sorted(hand.cards)

    same_value_cards_counter = 0
    current_card = sorted_hand[0]

    for card in sorted_hand:
        if card == current_card:
            same_value_cards_counter += 1
        else:
            if same_value_cards_counter == 2:
                for i in range(2):  # remove those 2 cards and check if there is a three too
                    hand.cards.remove(current_card)

                if check_three_of_a_kind(hand):
                    for i in range(2):  # place removed cards back
                        hand.cards.append(current_card)
                    return 1
                else:
                    for i in range(2):  # place removed cards back
                        hand.cards.append(current_card)
                    return 0

            current_card = card
            same_value_cards_counter = 1

        if same_value_cards_counter == 3:
            for i in range(3):  # remove those 3 cards and check if there is a pair too
                hand.cards.remove(current_card)

            if check_one_pair(hand):
                for i in range(3):  # place removed cards back
                    hand.cards.append(current_card)
                return 1
            else:
                for i in range(3):  # place removed cards back
                    hand.cards.append(current_card)
                return 0
    return 0

## Checks flush combination
def check_flush(hand):
    same_suit_quant = [0, 0, 0, 0]

    for card in hand.cards:
        for i in range(4):
            if card.suit == suits[i]:
                same_suit_quant[i] += 1

    for i in range(4):
        if same_suit_quant[i] > 4:
            # print('Flush')
            return 1
    return 0

## Checks straight combination
def check_straight(hand):
    sorted_hand = sorted(hand.cards)

    current_value = sorted_hand[0].value
    in_a_row_counter = 0

    for card in sorted_hand:
        if card.value == current_value:
            current_value += 1
            in_a_row_counter += 1
        elif card.value == current_value - 1:
            continue
        else:
            current_value = card.value
            in_a_row_counter = 1

    if in_a_row_counter > 4:
        # print('Straight')
        return 1

    return 0

## Checks three of a kind combination
def check_three_of_a_kind(hand):
    sorted_hand = sorted(hand.cards)

    current_value = sorted_hand[0].value
    same_value_cards_counter = 0

    for card in sorted_hand:
        if card.value == current_value:
            same_value_cards_counter += 1
            if same_value_cards_counter == 3:
                # print('Three of a kind')
                return 1
        else:
            current_value = card.value
            same_value_cards_counter = 1

    return 0

## Checks two pairs combination
def check_two_pairs(hand):
    sorted_hand = sorted(hand.cards)

    same_value_cards_counter = 0
    current_card = sorted_hand[0]

    for card in sorted_hand:
        if card == current_card:
            same_value_cards_counter += 1
        else:
            if same_value_cards_counter == 2:
                for i in range(2):  # remove those 2 cards
                    hand.cards.remove(current_card)

                if check_one_pair(hand):  # and check if there one more pair
                    # print("Two pairs")
                    return 1
                else:
                    return 0
            current_card = card
            same_value_cards_counter = 1
    return 0

## Checks paircombination
def check_one_pair(hand):  # returns the total_point and prints out 'One Pair' if true, if false, pass down to isHigh()
    if len(hand.cards) == 0:
        return 0

    sorted_hand = sorted(hand.cards)

    current_value = sorted_hand[0].value
    same_value_cards_counter = 0

    for card in sorted_hand:
        if card.value == current_value:
            same_value_cards_counter += 1
            if same_value_cards_counter == 2:
                # print('Two of a kind')
                return 1
        else:
            current_value = card.value
            same_value_cards_counter = 1

    return 0

## Checks highest card combination
def check_highest_card_value(hand):  # returns the value of the highest card
    sorted_hand = sorted(hand.cards)
    # print("Highest: " + str(sorted_hand[len(sorted_hand) - 1]))
    return sorted_hand[len(sorted_hand) - 1].value

## Class that defines Card-object
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

## Class that defines Deck-object
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.deck.append(card)

    ## Shuffles cards in deck
    def shuffle(self):
        random.shuffle(self.deck)

    ## Gets card from deck
    #  @return card from top of the deck
    def get_card(self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop()

    def __len__(self):
        return len(self.deck)

## Class that defines Hand-object
class Hand:
    def __init__(self):
        self.cards = []

    ## Adds card to hand
    def add_card(self, card):
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    ## Checks what combination this hand have with the board
    def check_combination(self, board):
        if check_royal_flush(self + board):
            return 9 + 14
        elif check_straight_flush(self + board):
            return 8 + 14
        elif check_four_of_a_kind(self + board):
            return 7 + 14
        elif check_full_house(self + board):
            return 6 + 14
        elif check_flush(self + board):
            return 5 + 14
        elif check_straight(self + board):
            return 4 + 14
        elif check_three_of_a_kind(self + board):
            return 3 + 14
        elif check_two_pairs(self + board):
            return 2 + 14
        elif check_one_pair(self + board):
            return 1 + 14
        else:
            return check_highest_card_value(self + board)

    def __add__(self, second):
        temp_hand = Hand()

        if len(self.cards) == 0:
            temp_hand = second
        elif len(second.cards) == 0:
            temp_hand = self
        else:
            for card in self.cards:
                temp_hand.add_card(card)
            for card in second.cards:
                temp_hand.add_card(card)

        return temp_hand

    def __str__(self):
        print_str = ""
        for card in self.cards:
            print_str += str(card) + ' '
        return print_str

    ## Checks if this hand combination is better than second hands combination
    def better_than(self, second_hand, board):
        return self.check_combination(board) > second_hand.check_combination(board)

    ## Checks if this hand combination is worse than second hands combination
    def worse_than(self, second_hand, board):
        return self.check_combination(board) < second_hand.check_combination(board)

    ## Checks if this hand combination is equal to second hands combination
    def equal_to(self, second_hand, board):
        return self.check_combination(board) == second_hand.check_combination(board)
