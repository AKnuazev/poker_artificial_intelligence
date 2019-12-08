import numpy as np
import random

import source.MCTS as mcts
from source.poker_game import Game
from source.poker_items import Card
import time
import matplotlib.pyplot as plt
from source.poker_items import Hand
from math import sqrt, pow
from source.settings import start_points


class User:
    def __init__(self, name="usual_player", points=start_points[0], hand=Hand(), board=Hand(), bet=0):
        # Own parameters
        self.name = name
        self.points = points
        self.hand = hand

        # Global parameters
        self.actions = {"pass": 0, "call": 1, "raise": 2}


class ConsolePlayer:
    def __init__(self, name="usual_player", points=start_points[0], hand=Hand(), board=Hand(), bet=0):
        # Own parameters
        self.name = name
        self.points = points
        self.hand = hand

        # Global parameters
        self.actions = {"pass": 0, "call": 1, "raise": 2}

    def act(self):
        return input('Enter action: ')


class Agent:
    def __init__(self, name, value_network, policy_network, hand=Hand(), board=Hand(), bet=0):
        self.name = name  # Player`s name
        self.actions = {"pass": 0, "call": 1, "raise": 2}

        self.points = start_points[1]
        self.hand = hand  # Player`s hand
        self.board = board  # Cards on board
        self.value_network = value_network  # Current value network model
        self.policy_network = policy_network  # Current policy network model

    def act(self, hand, board):
        state_value = self.evaluate_state(hand, board)

        if (state_value < 0.3):
            return self.actions["pass"]
        elif (state_value > 0.6):
            return self.ac

    def evaluate_state(self, hand, board):
        # Fill the board
        while (len(board.cards) != 5):
            board.add_card(Card(0, '0'))

        # State evaluation by two parameters
        value = self.value_network.predict(hand, board)
        policy = self.policy_network.predict()

        # Normalization
        if value < 15:
            value /= pow(2, 26)
        else:
            value = pow(2, value - 14) / pow(2, 23)

        policy /= 3

        # Combination of two rates
        state_quality = policy + value
