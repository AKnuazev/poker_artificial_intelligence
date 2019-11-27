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

    def act(self, state, tau):
        action = input('Enter action: ')
        pi = np.zeros(self.action_size)
        pi[action] = 1
        value = None
        NN_value = None
        return (action, pi, value, NN_value)


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

    def predict(self, model_input):
        predictions = self.model.predict(model_input)
        return predictions

    # def get_preds(self, state):

    def build_MCTS(self, state):
        self.root = mcts.Node(state)
        self.mcts = mcts.MCTS(self.root)

   # def evaluateLeaf(self, ):

