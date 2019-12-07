import numpy as np
import matplotlib.pyplot as plt
import source.settings as setts
from source.networks.value_network.value_network_model import ValueNetwork
from source.networks.policy_network.policy_network_model import PolicyNetwork
from source.poker_items import Hand, Deck

# plot example
# y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17, 20, 25, 40])
# x = np.arange(0, len(y))
# plt.plot(x, y)
# plt.show()


# path test
# f = open('value_network/training_1/cp.ckpt', 'w')

# Value-network training
value_network = ValueNetwork()
# value_network.start_training()
# value_network.visualize_studying_results()

# Policy-network training
policy_network = PolicyNetwork()
policy_network.start_training()
policy_network.visualize_studying_results()

# ---------------LOAD TEST ------------------------
# deck = Deck()
# deck.shuffle()
#
# hand1 = Hand()
# hand2 = Hand()
# board = Hand()
#
# for _ in range(2):
#     hand1.add_card(deck.get_card())
# for _ in range(2):
#     hand2.add_card(deck.get_card())
# for _ in range(5):
#     board.add_card(deck.get_card())
#
# value_network.load()
# policy_network.load()
#
# print("Hand 1:", hand1)
# print("Hand 2:", hand2)
# print("Board:", board)
# print()
#
# print("Value network:")
# print(value_network.predict(hand1, board))
# print(hand1.check_combination(board))
# print()
#
# print("Policy network:")
# print(policy_network.predict(hand1, board))
# print(hand1.better_than(hand2, board))

# -------------------NUMPY EXAMPLE--------------------
# a = [1, 2]
# b = [3, 4]

# c = np.array((a + b))
# print(c)
# print(c.size)
