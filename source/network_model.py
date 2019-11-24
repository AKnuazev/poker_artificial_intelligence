from keras import Sequential
from keras.layers.core import Dense

class MyNetwork:
    def __init__(self, input_dim,  output_dim, learning_rate):  # Later - more parameters
        self.model = Sequential()
        self.model.add(Dense(32, input_dim=input_dim, output_dim=output_dim, learning_rate = learning_rate))

