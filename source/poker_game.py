## @package source.poker_game
# @brief This part describes the basic gameplay, represented by two structural elements: Round and Game

from source.poker_items import Card, Deck, Hand
import numpy as np
from source.settings import start_points


##  Class that specifies round logic
class Round:
    def __init__(self, players, dealer_turn, players_number=2, cards_in_hand_number=2, deal_amount=50,
                 raise_size=25):
        # Round parameters
        self.player_turn = dealer_turn
        self.deal_amount = deal_amount
        self.raise_size = raise_size

        # Players
        self.players = players

        # Initialization
        self.bank = 0
        self.curr_bet = 0
        self.board = Hand()
        self.winner = 0

        # Prepare items
        self.deck = Deck()  # Make deck
        self.deck.shuffle()  # Shuffle
        self.hands = []  # Make two hands

        # Deal cards to players
        for i in range(players_number):
            curr_hand = Hand()
            for j in range(cards_in_hand_number):
                curr_hand.add_card(self.deck.get_card())
            self.hands.append(curr_hand)

        self.players[0].hand = self.hands[0]
        self.players[1].hand = self.hands[1]

        # Deal two first cards to board
        for i in range(2):
            self.board.add_card(self.deck.get_card())

    ## First round steps
    def start(self):
        # Deal points by dealer
        self.bank = 0
        self.bank += self.deal_amount
        self.curr_bet = self.deal_amount
        self.players[self.player_turn].points -= self.deal_amount
        self.players[self.player_turn].player_bet = self.deal_amount

        # Deal points by second player
        self.bank += self.deal_amount / 2
        self.players[1 - self.player_turn].points -= self.deal_amount / 2
        self.players[1 - self.player_turn].player_bet = self.deal_amount

    ## Makes changes to the playing position in accordance with the perfect action
    # @input Player action
    def take_action(self, curr_player, action):
        # 0 - pass
        # 1 - call
        # 2 - raise
        if action == 0:
            self.players[1 - curr_player].points += self.bank
            self.winner = 1 - curr_player
        elif action == 1:
            self.bank += self.curr_bet - self.players[curr_player].player_bet
            self.players[curr_player].points -= self.curr_bet - self.players[curr_player].player_bet
            self.players[curr_player].player_bet = self.curr_bet
        elif action == 2:
            self.curr_bet = self.players[curr_player].player_bet + self.raise_size
            self.bank += self.curr_bet - self.players[curr_player].player_bet
            self.players[curr_player].points -= self.curr_bet - self.players[curr_player].player_bet
            self.players[curr_player].player_bet=self.curr_bet


    ## Opens one more card on board
    def open_card(self):
        self.board.add_card(self.deck.get_card())

    ## Calculates the results of round, makes changes in points
    def summarize(self):
        if self.hands[0].better_than(self.hands[1], self.board):
            self.winner = 2
            self.players[0].points += self.bank
        elif self.hands[0].worse_than(self.hands[1], self.board):
            self.winner = 0
            self.players[1].points += self.bank
        elif self.hands[0].equal_to(self.hands[1], self.board):
            self.winner = 1
            self.players[0].points += self.bank / 2
            self.players[1].points += self.bank / 2

        return self.winner


## Class that specifies the connection in sequence of rounds (full game)
class Game:
    def __init__(self, player1, player2, points=start_points):
        # Game settings
        self.points = points  # Players points at the beginning
        self.actions = [0, 1, 2, 3]
        self.actions_number = len(self.actions)

        # Prepare items
        self.deck = Deck()  # Make deck
        self.deck.shuffle()  # Shuffle

        # Initialization
        self.player_turn = 0

        # Statistics
        self.winning_history = []
        self.points_history = []

    ## Adds the result of the round to game
    def add_round(self, winner, players_points):
        self.winning_history.append(winner)
        self.points_history.append((players_points[0], players_points[1]))
