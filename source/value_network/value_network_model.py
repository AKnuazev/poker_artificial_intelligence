from keras.layers.core import Dense
from keras.models import Sequential, load_model, Model
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint

from source.value_network.value_network_settings import VALUE_HIDDEN_LAYERS_QUANTITY, VALUE_NEURONS_QUANTITY
from source.value_network.value_network_settings import VALUE_BATCH_SIZE, VALUE_DATASET_SIZE, VALUE_EPOCHS

from source.poker_game import Game, GameState
from source.poker_items import Deck, Hand, Card
from math import log2, pow

import random
import matplotlib.pyplot as plt
import numpy as np
import os


class ValueNetwork:
    def __init__(self):  # Later - more parameters
        self.history = None

        self.checkpoint_path = "training_1/cp.ckpt"
        self.checkpoint_dir = os.path.dirname(self.checkpoint_path)

        self.layers_quant = VALUE_HIDDEN_LAYERS_QUANTITY
        self.neurons_quant = VALUE_NEURONS_QUANTITY

        self.model = Sequential()

        # Input layer
        self.model.add(Dense(14, input_shape=(1,)))

        # Hidden layers
        for _ in range(VALUE_HIDDEN_LAYERS_QUANTITY):
            self.model.add(Dense(VALUE_NEURONS_QUANTITY, activation='relu'))

        # Output layer
        self.model.add(Dense(1, activation='relu'))  # from -12 to 9

        # Compile model
        self.model.compile(loss='MSE', optimizer='sgd', metrics=['accuracy'])

    def create_full_dataset(self):
        training_set = []
        true_combinations_set = []

        for _ in range(VALUE_DATASET_SIZE):
            train, combination = self.create_train()
            training_set.append(train)
            true_combinations_set.append(combination)

        numpy_training_set = np.array(training_set)
        numpy_true_combinations_set = np.array(true_combinations_set)

        return numpy_training_set, numpy_true_combinations_set

    def create_train(self):
        train = []
        open_cards_quantity = random.randint(2, 5)
        deck = Deck()
        deck.shuffle()

        state = Hand()
        for _ in range(7):
            state.add_card(deck.get_card())

        for i in range(2 + open_cards_quantity):
            train.append(state.cards[i])
        for _ in range(5 - open_cards_quantity):
            train.append(Card(0, '0'))

        combination = state.check_combination(Hand())

        values = []
        suits = []
        for card in train:
            values.append(card.value)

            # suits = ["♠", "♣", "♥", "♦"]  # "spades", " clubs", "hearts", "diamonds"
            if card.suit == "♠":
               suits.append(0)
            elif card.suit == "♣":
                suits.append(1)
            elif card.suit == "♥":
                suits.append(2)
            elif card.suit == "♦":
                suits.append(3)

        # numpy_train = np.array([values, suits])  # Convert our array to numpy array
        numpy_train = np.array(values + suits)  # Convert our array to numpy array
        # combination = np.array([combination, 0, 0])  # Reshape
        return numpy_train, combination

    def start_training(self):
        checkpoint_callback = ModelCheckpoint(filepath=self.checkpoint_path, save_weights_only=True, verbose=1)
        training_set, true_results_set = self.create_full_dataset()
        # true_results_set = true_results_set.reshape(10000, 1, 1)
        self.history = self.model.fit(training_set, true_results_set,epochs=VALUE_EPOCHS, batch_size=VALUE_BATCH_SIZE, callbacks=[checkpoint_callback])

    def visualize_studying_results(self):
        y = self.history
        x = len(y)
        plt.plot(x, y)
        plt.show()

    def predict(self, some_state_parametrs):
        return self.model.predict(some_state_parametrs)

    def load(self):
        return self.model.load_weights(self.checkpoint_path)
