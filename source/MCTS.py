import numpy as np
from source.poker_game import Game
from source.settings import start_points


# Ysel
class Node:
    def __init__(self, state, parent_node=None, parent_edge=None):
        self.state = state
        self.player_turn = state.player_turn

        self.parent_node = parent_node
        self.parent_edge = parent_edge
        self.child_nodes = []
        self.child_edges = []

        self.stats = {
            'N': 0,  # How many times have we walked on this node
            'W': 0,  # The value of this node
            'Q': 0,  # Average value of all child nodes of this node
            'P': 0  # The probability that out of all the nodes allowed on this move we will choose this
        }

    def is_leaf(self):
        if len(self.child_edges) > 0:
            return False
        else:
            return True

    def add_child(self, node, probability, action):
        self.child_nodes.append(node)
        self.child_edges.append(Edge(node, self, probability, action))

        node.parent_edge = self


# Rebro
class Edge:
    def __init__(self, in_node, out_node, prior, action):
        self.in_node = in_node
        self.out_node = out_node
        self.player_turn = in_node.state.player_turn
        self.action = action


# Tree
class Tree:
    def __init__(self, start_state):
        self.game = Game(start_points)
        self.root = Node(start_state)
        self.lengths = []

        # Building tree
        for layer in range(self.game.actions_number*2):                 # 9
            self.lengths.append(pow(self.game.actions_number, layer))   # 4


    def __len__(self):
        return len(self.tree)

    # def move_to_leaf(self):

    # def back_fill(self, ...):

    # def get_action(self, ...):
