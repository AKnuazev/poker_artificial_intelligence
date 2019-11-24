import numpy as np
import random

import source.MCTS as mcts
from source.poker_game import Game

import time
import matplotlib.pyplot as plt


class User:
    def __init__(self, name, states, actions):
        self.name = name
        self.states = states
        self.actions = actions


class Agent:
    def __init__(self, name, states, actions, model):
        self.name = name

        self.states = states
        self.actions = actions

        self.model = model

    # def simulate(self):

    # def replay(self, ):

    # def chooseAction(self, ):

    # def act(self, ):

    def predict(self, input_to_model):
        predictions = self.model.predict(input_to_model)
        return predictions

    # def get_preds(self, state):

    def build_MCTS(self, state):
        self.root = mcts.Node(state)
        self.mcts = mcts.MCTS(self.root)

   # def evaluateLeaf(self, ):

