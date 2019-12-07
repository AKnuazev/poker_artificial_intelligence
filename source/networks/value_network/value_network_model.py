from keras.layers.core import Dense
from keras.models import Sequential, load_model, Model
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint

from source.networks.value_network.value_network_settings import VALUE_HIDDEN_LAYERS_QUANTITY, VALUE_NEURONS_QUANTITY
from source.networks.value_network.value_network_settings import VALUE_BATCH_SIZE, VALUE_DATASET_SIZE, VALUE_EPOCHS

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

        self.checkpoint_path = "networks/value_network/trainings/training_1/cp.ckpt"
        self.checkpoint_dir = os.path.dirname(self.checkpoint_path)

        self.layers_quant = VALUE_HIDDEN_LAYERS_QUANTITY
        self.neurons_quant = VALUE_NEURONS_QUANTITY

        self.model = Sequential()

        # Input layer
        self.model.add(Dense(14, input_dim=14))

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
            if card.suit == '0':
                suits.append(0)
            elif card.suit == "♠":
                suits.append(1)
            elif card.suit == "♣":
                suits.append(2)
            elif card.suit == "♥":
                suits.append(3)
            elif card.suit == "♦":
                suits.append(4)

        # numpy_train = np.array([values, suits])  # Convert our array to numpy array
        numpy_train = np.array(values + suits)  # Convert our array to numpy array
        # combination = np.array([combination, 0, 0])  # Reshape
        return numpy_train, combination

    def start_training(self):
        checkpoint_callback = ModelCheckpoint(filepath=self.checkpoint_path, save_weights_only=True, verbose=1)
        training_set, true_results_set = self.create_full_dataset()
        # true_results_set = true_results_set.reshape(10000, 1, 1)
        self.history = self.model.fit(training_set, true_results_set, epochs=VALUE_EPOCHS, batch_size=VALUE_BATCH_SIZE,
                                      callbacks=[checkpoint_callback])

    def visualize_studying_results(self):
        # print(self.history.history.keys())
        # summarize history for accuracy
        plt.plot(self.history.history['accuracy'])
        # plt.plot(self.history.history['val_accuracy'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        # self.history.history[]
        # summarize history for loss
        plt.plot(self.history.history['loss'])
        # plt.plot(self.history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()

    def predict(self, hand, board):
        values = []
        suits=[]
        for card in hand.cards:
            values.append(card.value)

            if card.suit == '0':
                suits.append(0)
            elif card.suit == "♠":
                suits.append(1)
            elif card.suit == "♣":
                suits.append(2)
            elif card.suit == "♥":
                suits.append(3)
            elif card.suit == "♦":
                suits.append(4)

        for card in board.cards:
            values.append(card.value)

            if card.suit == '0':
                suits.append(0)
            elif card.suit == "♠":
                suits.append(1)
            elif card.suit == "♣":
                suits.append(2)
            elif card.suit == "♥":
                suits.append(3)
            elif card.suit == "♦":
                suits.append(4)

        input = np.array([values+suits])
        return self.model.predict(input)

    def load(self):
        return self.model.load_weights(self.checkpoint_path)
