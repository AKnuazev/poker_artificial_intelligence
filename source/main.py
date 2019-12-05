import numpy as np
import matplotlib.pyplot as plt
import source.settings as setts
from source.value_network.value_network_model import ValueNetwork

# plot example
# y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17, 20, 25, 40])
# x = np.arange(0, len(y))
# plt.plot(x, y)
# plt.show()



# path test
# f = open('value_network/training_1/cp.ckpt', 'w')

# Network training
best_network = ValueNetwork()
best_network.start_training()
best_network.visualize_studying_results()

# numpy example
# a = [1, 2]
# b = [3, 4]
#
# c = np.array((a + b))
# print(c)
# print(c.size)
