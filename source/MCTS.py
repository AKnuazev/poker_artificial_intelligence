import numpy as np

# Ysel
class Node():
    def __init__(self, state):
        self.state = state
        self.player_turn = state.player_turn
        self.edges = []

    def is_leaf(self):
        if len(self.edges) > 0:
            return False
        else:
            return True

# Rebro
class Edge():
    def __init__(self, inNode, outNode, prior, action):
        self.inNode = inNode
        self.outNode = outNode
        self.playerTurn = inNode.state.playerTurn
        self.action = action

        self.stats = {
            'N': 0,
            'W': 0,
            'Q': 0,
            'P': prior,
        }


class MCTS():

    def __init__(self, root):
        self.root = root
        self.tree = {}
        # self.addNode(root)

    def __len__(self):
        return len(self.tree)

    # def moveToLeaf(self):

    # def backFill(self, ):

    # def add_node(self, node):