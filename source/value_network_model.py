from keras.layers.core import Dense
from keras.models import Sequential, load_model, Model
from keras.optimizers import sgd
from keras.callbacks import ModelCheckpoint

from source.settings import run_folder, run_archive_folder
from source.settings import VALUE_HIDDEN_LAYERS_QUANTITY, VALUE_NEURONS_QUANTITY
from source.settings import VALUE_BATCH_SIZE, VALUE_DATASET_SIZE, VALUE_EPOCHS

from source.poker_game import Game, GameState
from source.poker_items import Deck, Hand
from math import log2, pow

import random
import matplotlib.pyplot as plt
import numpy as np


class ValueNetwork:
    def __init__(self, input_dim, output_dim, learning_rate):  # Later - more parameters
        self.history = None
        self.layers_quant = VALUE_HIDDEN_LAYERS_QUANTITY
        self.neurons_quant = VALUE_NEURONS_QUANTITY

        self.model = Sequential()

        # Input layer
        self.model.add(Dense(14, input_shape=(14,)))

        # Hidden layers
        for _ in range(VALUE_HIDDEN_LAYERS_QUANTITY):
            self.model.add(Dense(VALUE_NEURONS_QUANTITY, activation='relu'))

        # Output layer
        self.model.add(Dense(22, activation='relu'))  # from -12 to 9

        # Compile model
        self.model.compile(loss='MSE', optimizer=sgd, metrics=['accuracy'])

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

        state = Hand()
        for _ in range(7):
            state.add_card(deck.get_card())

        for i in range(2 + open_cards_quantity):
            train.append(state.cards[i])
        for _ in range(5 - open_cards_quantity):
            train.append(0)

        combination = state.check_combination()

        numpy_train = np.array(train)  # Convert our array to numpy array
        return numpy_train, combination

    def start_training(self):

        training_set, true_results_set = self.create_full_dataset()
        self.history = self.model.fit(training_set, true_results_set, batch_size=VALUE_BATCH_SIZE, epochs=VALUE_EPOCHS)

    def visualize_studying_results(self):
        y = self.history
        x = len(y)
        plt.plot(x, y)
        plt.show()

    def predict(self, some_state_parametrs):
        return self.model.predict(some_state_parametrs)

    def save(self, game, version):
        self.model.save(run_folder + 'models/version' + version + '.h5')

    def load(self, game, run_number, version):
        return load_model(run_archive_folder + ...)
