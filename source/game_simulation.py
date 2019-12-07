from source.poker_game import Game
from source.settings import start_points
from source.agent import Agent
from source.settings import EPISODES, start_points
from uis.poker_gui import Ui_MainWindow
from PyQt5 import QtWidgets

class Match:
    def __init__(self, player1, player2, curr_start_points=start_points):
        super(Match, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals to functions
        self.ui.PassButton.clicked.connect(self.pass_clicked)
        self.ui.CallButton.clicked.connect(self.call_clicked)
        self.ui.RaiseButton.clicked.connect(self.raise_clicked)


        self.player1 = player1
        self.player2 = player2
        self.points = curr_start_points
        self.player1_action=3

    def pass_clicked(self):
        self.player1_action = 0

    def call_clicked(self):
        self.player1_action = 1

    def raise_clicked(self):
        self.player1_action = 2

    def start_match(player1, player2):
        

        # for curr_episode in range(EPISODES):

        return



