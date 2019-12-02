from keras.layers.core import Dense
from keras.models import Sequential, load_model, Model
from source.settings import run_folder, run_archive_folder

from math import log2, pow


class MyNetwork:
    def __init__(self, input_dim, output_dim, learning_rate):  # Later - more parameters
        self.model = Sequential()
        self.model.add(Dense(32, input_dim=input_dim, output_dim=output_dim, learning_rate=learning_rate))

    def loss_function(self, z, v, pi, T, p, tau):
        return pow((z - v), 2) - pow(pi, T) * log2(p) + pow(tau, 2)

    def predict(self, some_state_parametrs):
        return self.model.predict(some_state_parametrs)

    def fit(self, some_state_parametrs):
        return self.model.fit(some_state_parametrs)

    def write(self, game, version):
        self.model.save(run_folder + 'models/version' + version + '.h5')

    def read(self, game, run_number, version):
        return load_model(run_archive_folder + ...)
