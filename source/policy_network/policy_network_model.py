from keras.layers.core import Dense
from keras.models import Sequential, load_model, Model
from source.settings import run_folder, run_archive_folder
from source.settings import POLICY_HIDDEN_LAYERS_QUANTITY, POLICY_NEURONS_QUANTITY
from source.poker_game import Game, GameState

from math import log2, pow


class PolicyNetwork:
    def __init__(self, input_dim, output_dim, learning_rate):  # Later - more parameters
        self.model = Sequential()

        for _ in range(HIDDEN_LAYERS_QUANTITY):
            self.model.add(Dense(32, input_dim=input_dim, output_dim=output_dim, learning_rate=learning_rate))

    def loss_function(self, y_true, y_pred):
        return pow((z - v), 2) - pow(pi, T) * log2(p) + pow(tau, 2)

    def predict(self, some_state_parametrs):
        return self.model.predict(some_state_parametrs)

    def fit(self, some_state_parametrs):
        return self.model.fit(some_state_parametrs)

    def write(self, game, version):
        self.model.save(run_folder + 'models/version' + version + '.h5')

    def read(self, game, run_number, version):
        return load_model(run_archive_folder + ...)
