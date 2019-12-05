from keras.layers.core import Dense
from keras.models import Sequential, load_model, Model
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint

from source.networks.policy_network.policy_network_settings import POLICY_HIDDEN_LAYERS_QUANTITY, \
    POLICY_NEURONS_QUANTITY
from source.networks.policy_network.policy_network_settings import POLICY_BATCH_SIZE, POLICY_DATASET_SIZE, POLICY_EPOCHS

from source.poker_game import Game, GameState
from source.poker_items import Deck, Hand, Card
from math import log2, pow

import random
import matplotlib.pyplot as plt
import numpy as np
import os


class PolicyNetwork:
    def __init__(self):  # Later - more parameters
        self.history = None

        self.checkpoint_path = "policy_network/training_1/cp.ckpt"
        self.checkpoint_dir = os.path.dirname(self.checkpoint_path)

        self.layers_quant = POLICY_HIDDEN_LAYERS_QUANTITY
        self.neurons_quant = POLICY_NEURONS_QUANTITY

        self.model = Sequential()

        # Input layer
        self.model.add(Dense(14, input_dim=14))

        # Hidden layers
        for _ in range(POLICY_HIDDEN_LAYERS_QUANTITY):
            self.model.add(Dense(POLICY_NEURONS_QUANTITY, activation='relu'))

        # Output layer
        self.model.add(Dense(1, activation='relu'))  # from -12 to 9

        # Compile model
        self.model.compile(loss='MSE', optimizer='sgd', metrics=['accuracy'])

    def create_full_dataset(self):
        training_set = []
        true_results_set = []

        for _ in range(POLICY_DATASET_SIZE):
            train, combination = self.create_train()
            training_set.append(train)
            true_results_set.append(combination)

        numpy_training_set = np.array(training_set)
        numpy_true_combinations_set = np.array(true_results_set)

        return numpy_training_set, numpy_true_combinations_set

    def create_train(self):
        train = []
        open_cards_quantity = random.randint(2, 5)
        deck = Deck()
        deck.shuffle()

        hand1 = Hand()
        hand2 = Hand()
        board = Hand()

        for i in range(2):
            hand1.add_card(deck.get_card())
        for i in range(2):
            hand1.add_card(deck.get_card())
        for i in range(5):
            board.add_card(deck.get_card())

        round_result = 0
        if hand1.better_than(hand2, board):
            round_result = 1
        elif hand1.worse_than(hand2, board):
            round_result = -1
        elif hand1.equal_to(hand2, board):
            round_result = 0

        values = []
        suits = []

        # In hand 1
        for card in hand1.cards:
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

        # In hand 2
        for card in hand2.cards:
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

        # In board
        for i in range(open_cards_quantity):
            values.append(board.cards[i].value)

            # suits = ["♠", "♣", "♥", "♦"]  # "spades", " clubs", "hearts", "diamonds"
            if board.cards[i].suit == '0':
                suits.append(0)
            elif board.cards[i].suit == "♠":
                suits.append(1)
            elif board.cards[i].suit == "♣":
                suits.append(2)
            elif board.cards[i].suit == "♥":
                suits.append(3)
            elif board.cards[i].suit == "♦":
                suits.append(4)

        numpy_train = np.array(values + suits)  # Convert our array to numpy array
        return numpy_train, round_result

    def start_training(self):
        checkpoint_callback = ModelCheckpoint(filepath=self.checkpoint_path, save_weights_only=True, verbose=1)
        training_set, true_results_set = self.create_full_dataset()
        # true_results_set = true_results_set.reshape(10000, 1, 1)
        self.history = self.model.fit(training_set, true_results_set, epochs=POLICY_EPOCHS,
                                      batch_size=POLICY_BATCH_SIZE,
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

    def predict(self, some_state_parametrs):
        return self.model.predict(some_state_parametrs)

    def load(self):
        return self.model.load_weights(self.checkpoint_path)
