from source.poker_game import Game, Round

from source.settings import start_points
from source.agent import Agent, User
from source.settings import EPISODES, start_points
from uis.poker_gui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel

from source.networks.value_network.value_network_model import ValueNetwork
from source.networks.policy_network.policy_network_model import PolicyNetwork


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
        self.player1_action = 3

        self.human_act_status = 3  # 3 means no action recorded

        # Networks activation
        self.value_network=ValueNetwork()
        self.value_network.load()

        self.policy_network=PolicyNetwork()
        self.policy_network.load()

    def pass_clicked(self):
        self.human_act_status = 0

    def call_clicked(self):
        self.human_act_status = 1

    def raise_clicked(self):
        self.human_act_status = 2

    def start_match(self):
        user = User("human")
        opponent = Agent("AI", ValueNetwork, PolicyNetwork)

        game = Game(user, opponent)

        while self.player1.points > 0 and self.player2.points > 0:
            round = Round(user, opponent, game.player_turn)

            for step in range(4):
                if game.player_turn == 0:
                    # Waiting for response
                    while self.human_act_status == 3:
                        self.ui.statusbar.addWidget(QLabel("Waiting for human step..."))

                    # Acting
                    round.take_action(0, self.human_act_status)
                    round.take_action(1, opponent.act(opponent.hand, round.board))

                    # Reset act status and switch turn
                    self.human_act_status = 3
                    game.player_turn = 1

                elif game.player_turn == 1:
                    # Opponent acting
                    round.take_action(1, opponent.act(opponent.hand, round.board))

                    # Waiting for response
                    while self.human_act_status == 3:
                        self.ui.statusbar.addWidget(QLabel("Waiting for human step..."))

                    # Human acting
                    round.take_action(0, self.human_act_status)

                    # Reset act status and switch turn
                    self.human_act_status = 3
                    game.player_turn = 1
