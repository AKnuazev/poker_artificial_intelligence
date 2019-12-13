## @package policy_network_model
# @brief A model of a neural network policy that assesses the current state in the
# form of a prediction of the expected outcome of a round (win / draw / loss)

from keras.layers.core import Dense, Dropout
from keras.models import Sequential, load_model, Model
from keras.callbacks import ModelCheckpoint
from source.networks.policy_network.policy_network_settings import POLICY_HIDDEN_LAYERS_QUANTITY, \
    POLICY_NEURONS_QUANTITY
from source.networks.policy_network.policy_network_settings import POLICY_BATCH_SIZE, POLICY_DATASET_SIZE, POLICY_EPOCHS
from source.poker_items import Deck, Hand, Card

import random
import matplotlib.pyplot as plt
import numpy as np
import os

## Policy network model class
class PolicyNetwork:
    def __init__(self):  # Later - more parameters
        self.history = None

        self.checkpoint_path = "networks/policy_network/trainings/training_2/cp.ckpt"
        self.checkpoint_abs_path = os.path.abspath(self.checkpoint_path)

        self.layers_quant = POLICY_HIDDEN_LAYERS_QUANTITY
        self.neurons_quant = POLICY_NEURONS_QUANTITY

        self.model = Sequential()

        # Input layer
        self.model.add(Dense(14, input_dim=14))

        # Hidden layers
        for i in range(POLICY_HIDDEN_LAYERS_QUANTITY):
            self.model.add(Dense(POLICY_NEURONS_QUANTITY, activation='relu'))
            self.model.add(Dropout(0.2))

        # Output layer
        self.model.add(Dense(1, activation='relu'))  # from -12 to 9

        # Compile model
        self.model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    ## Function that creates full dataset with fixed size
    # @input The size of needed dataset
    # @return Game situation (array of cards) and true value won/draw/lost
    def create_full_dataset(self, size=POLICY_DATASET_SIZE):

        training_set = []
        true_results_set = []

        for _ in range(size):
            train, result = self.create_train()
            training_set.append(train)
            true_results_set.append(result)

        numpy_training_set = np.array(training_set)
        numpy_true_results_set = np.array(true_results_set)

        return numpy_training_set, numpy_true_results_set

    ## Function that creates one random game position
    # @return Game situation (array of cards) and true value won/draw/lost
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
            hand2.add_card(deck.get_card())
        for i in range(5):
            board.add_card(deck.get_card())

        round_result = 0
        if hand1.better_than(hand2, board):
            round_result = 2  # Player wins
        elif hand1.worse_than(hand2, board):
            round_result = 0  # Opponent wins
        elif hand1.equal_to(hand2, board):
            round_result = 1  # Draw

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

        # In board
        for i in range(open_cards_quantity):
            values.append(board.cards[i].value)

            # suits = ["♠", "♣", "♥", "♦"]  # "spades", " clubs", "hearts", "diamonds"

            if board.cards[i].suit == "♠":
                suits.append(1)
            elif board.cards[i].suit == "♣":
                suits.append(2)
            elif board.cards[i].suit == "♥":
                suits.append(3)
            elif board.cards[i].suit == "♦":
                suits.append(4)
        for i in range(5 - open_cards_quantity):
            values.append(0)
            suits.append(0)

        numpy_train = np.array(values + suits)  # Convert our array to numpy array
        # numpy_train = np.array(values)
        # print(numpy_train.shape)
        return numpy_train, round_result

    ## Function that starts network training
    def start_training(self):
        checkpoint_callback = ModelCheckpoint(filepath=self.checkpoint_path, save_weights_only=True, verbose=1)
        training_set, true_results_set = self.create_full_dataset()
        # true_results_set = true_results_set.reshape(10000, 1, 1)
        self.history = self.model.fit(training_set, true_results_set, epochs=POLICY_EPOCHS,
                                      batch_size=POLICY_BATCH_SIZE,
                                      callbacks=[checkpoint_callback])

    ## A function that visualizes the results of the last training session in the form of graphs of changes in
    # accuracy and losses over time
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

    ## A function that evaluates the policy for the transferred game state
    # @param hand: Cards in players hand
    # @param board: Cards on board (the unknown are coded as 00)
    # @return The policy value of the current state
    def predict(self, hand, board):
        values = []
        suits = []

        for card in hand.cards:
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

        for card in board.cards:
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

        input = np.array([values + suits])

        return self.model.predict(input)

    ## A function that evaluates the current version of network
    # @return Average accuracy and loss for a random test data set
    def evaluate(self):
        x_test, y_test = self.create_full_dataset(10000)
        value = self.model.evaluate(x_test, y_test, 1000)
        return value

    ## Function loading the weights of the latest trained version of the neural network
    # @param path: The path to the weight data directory
    def load(self, path=None):
        if path == None:
            path = self.checkpoint_path
        self.model.load_weights(path)
