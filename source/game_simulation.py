from source.poker_game import Game, Round
import sys  # for argv transferring to QApplication
from source.settings import start_points
from source.agent import Agent, User
from source.settings import EPISODES, start_points
from uis.poker_gui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMessageBox

from source.networks.value_network.value_network_model import ValueNetwork
from source.networks.policy_network.policy_network_model import PolicyNetwork
from uis import poker_gui


class MainWindow(QtWidgets.QMainWindow, poker_gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals to functions
        self.ui.PassButton.clicked.connect(self.pass_clicked)
        self.ui.CallButton.clicked.connect(self.call_clicked)
        self.ui.RaiseButton.clicked.connect(self.raise_clicked)
        self.ui.actionNew_game.triggered.connect(self.start_session)
        self.ui.actionSave_report.triggered.connect(self.save_report)
        self.ui.actionExit.triggered.connect(self.close)

        self.is_session_active = 0
        self.human_act_status = 3  # 3 means no action recorded

        self.report_text = []

    def pass_clicked(self):
        self.human_act_status = 0
        self.ui.statusbar.showMessage("Human passed")

    def call_clicked(self):
        self.human_act_status = 1
        self.ui.statusbar.showMessage("Human called")

    def raise_clicked(self):
        self.human_act_status = 2
        self.ui.statusbar.showMessage("Human raised")

    def start_session(self):
        if self.is_session_active == 0:
            self.is_session_active = 1
            self.start_match()

    def save_report(self):
        file = open("reports\\report.txt", 'w')
        file.writelines(self.report_text)
        file.close()

    def start_match(self):
        self.user = User("human")
        self.opponent = Agent("AI", ValueNetwork, PolicyNetwork)

        self.ui.PlayerScoreNumber.setText(str(self.user.points))
        self.ui.OpponentScoreNumber.setText(str(self.opponent.points))

        game = Game(self.user, self.opponent)

        while self.user.points > 0 and self.opponent.points > 0:
            round = Round([self.user, self.opponent], game.player_turn)
            round.start()

            for step in range(4):
                # Set some info text
                self.ui.PlayerScoreNumber.setText(str(self.user.points))
                self.ui.OpponentScoreNumber.setText(str(self.opponent.points))
                self.ui.BetValueNumber.setText(str(round.curr_bet))

                self.ui.card1_hand1.setText(str(self.user.hand.cards[0]))
                self.ui.card2_hand1.setText(str(self.user.hand.cards[1]))

                self.ui.card1_board.setText(str(round.board.cards[0]))
                self.ui.card2_board.setText(str(round.board.cards[1]))
                if step > 0:
                    self.ui.card3_board.setText(str(round.board.cards[2]))
                if step > 1:
                    self.ui.card4_board.setText(str(round.board.cards[3]))
                if step > 2:
                    self.ui.card5_board.setText(str(round.board.cards[4]))

                # Make steps
                if game.player_turn == 0:
                    # Waiting for response
                    while self.human_act_status == 3:
                        QCoreApplication.processEvents()
                        self.ui.statusbar.showMessage("waiting, now: " + str(self.human_act_status))

                    # Acting
                    action = self.human_act_status
                    round.take_action(0, action)
                    self.report_text.append(str(action)+'\n')
                    self.ui.ReportText.addItem(str(action))
                    if action == 0:
                        self.report_text.append("AI wins"+'\n')
                        self.ui.ReportText.addItem("AI wins")
                        self.human_act_status = 3
                        game.player_turn = 1
                        break

                    action = self.opponent.act(self.opponent.hand, round.board)
                    round.take_action(1, action)
                    self.report_text.append(str(action) + '\n')
                    self.ui.ReportText.addItem(str(action))
                    if action == 0:
                        self.report_text.append("Human wins" + '\n')
                        self.ui.ReportText.addItem("Human wins")
                        self.human_act_status = 3
                        game.player_turn = 1
                        break

                    # Reset act status and switch turn
                    self.human_act_status = 3
                    game.player_turn = 1

                elif game.player_turn == 1:
                    # Acting
                    action = self.opponent.act(self.opponent.hand, round.board)
                    round.take_action(1, action)
                    self.report_text.append(str(action) + '\n')
                    self.ui.ReportText.addItem(str(action))
                    if action == 0:
                        self.report_text.append("Human wins" + '\n')
                        self.ui.ReportText.addItem("Human wins")
                        self.human_act_status = 3
                        game.player_turn = 0
                        break

                    # Waiting for response
                    while self.human_act_status == 3:
                        QCoreApplication.processEvents()
                        self.ui.statusbar.showMessage("waiting, now: " + str(self.human_act_status))

                    action = self.human_act_status
                    round.take_action(0, action)
                    self.report_text.append(str(action) + '\n')
                    self.ui.ReportText.addItem(str(action))
                    if action == 0:
                        self.report_text.append("AI wins" + '\n')
                        self.ui.ReportText.addItem("AI wins")
                        self.human_act_status = 3
                        game.player_turn = 0
                        break

                    # Reset act status and switch turn
                    self.human_act_status = 3
                    game.player_turn = 0

                round.open_card()

            self.ui.card1_hand1.clear()
            self.ui.card2_hand1.clear()

            self.ui.card1_board.clear()
            self.ui.card2_board.clear()
            self.ui.card3_board.clear()
            self.ui.card4_board.clear()
            self.ui.card5_board.clear()


class Match():
    def __init__(self, player1, player2, curr_start_points=start_points):
        self.player1 = player1
        self.player2 = player2
        self.points = curr_start_points
        self.player1_action = 3

        # Networks activation
        self.value_network = ValueNetwork()
        self.value_network.load()

        self.policy_network = PolicyNetwork()
        self.policy_network.load()

        # Application setup
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        self.window = MainWindow()  # Создаём объект класса MainWindow
        self.window.showFullScreen()  # Показываем окно

        app.exec()
