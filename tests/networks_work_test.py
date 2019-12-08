import unittest
import sys

sys.path.append("..")
from source.networks.policy_network.policy_network_model import PolicyNetwork


# from source.networks.value_network.value_network_model import ValueNetwork
# from source.poker_items import Hand


class TestPolicyNetwork(unittest.TestCase):
    def test_training_set_shapes(self):
        policy_network = PolicyNetwork()

        train, result = policy_network.create_train()
        self.assertEqual(train.shape, (14,))

        dataset, results = policy_network.create_full_dataset(10)
        self.assertEqual(dataset.shape, (10, 14,))

    def test_network_values_test(self):
        policy_network = PolicyNetwork()
        policy_network.checkpoint_abs_path = policy_network.checkpoint_abs_path.replace("tests\\", 'source\\')
        print(policy_network.checkpoint_abs_path)
        policy_network.load(policy_network.checkpoint_abs_path)

        value = policy_network.evaluate()
        print(value)
        self.assertLess(value[0], 2)
        self.assertLess(0.4, value[1])


if __name__ == "__main__":
    unittest.main()
