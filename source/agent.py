import numpy as np
import random

import source.MCTS as mcts
from source.poker_game import Game
import time
import matplotlib.pyplot as plt
from source.poker_items import Hand


class User:
    def __init__(self, name, states, actions):
        self.name = name
        self.states = states
        self.actions = actions

    def act(self):
        return input('Enter action: ')


class Agent:
    def __init__(self, name, hand, board, bet, model):
        self.name = name

        self.hand = hand
        self.board = board
        self.bet = bet
        self.model = model

    # def simulate(self):

    # def replay(self, ):

    # def chooseAction(self, ):

    def act(self, state):
        return mcts.get_action(state)


    def predict(self, model_input):
        predictions = self.model.predict(model_input)
        return predictions

    # def get_preds(self, state):

    def build_MCTS(self, state):
        self.root = mcts.Node(state)
        self.mcts = mcts.MCTS(self.root)

# def evaluateLeaf(self, ):
