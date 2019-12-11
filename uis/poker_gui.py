# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anton\PycharmProjects\course_work\uis\poker_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QtCore.QSize(1340, 960))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SettingsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SettingsBox.setGeometry(QtCore.QRect(100, 570, 291, 191))
        self.SettingsBox.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.SettingsBox.setObjectName("SettingsBox")
        self.PlayerScoreLabel = QtWidgets.QLabel(self.SettingsBox)
        self.PlayerScoreLabel.setGeometry(QtCore.QRect(20, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.PlayerScoreLabel.setFont(font)
        self.PlayerScoreLabel.setStyleSheet("font: 900 12pt \"Perpetua Titling MT\";")
        self.PlayerScoreLabel.setObjectName("PlayerScoreLabel")
        self.BetValueLabel = QtWidgets.QLabel(self.SettingsBox)
        self.BetValueLabel.setGeometry(QtCore.QRect(20, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.BetValueLabel.setFont(font)
        self.BetValueLabel.setStyleSheet("font: 900 12pt \"Perpetua Titling MT\";")
        self.BetValueLabel.setObjectName("BetValueLabel")
        self.OpponentScoreLabel = QtWidgets.QLabel(self.SettingsBox)
        self.OpponentScoreLabel.setGeometry(QtCore.QRect(20, 80, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.OpponentScoreLabel.setFont(font)
        self.OpponentScoreLabel.setStyleSheet("font: 900 12pt \"Perpetua Titling MT\";")
        self.OpponentScoreLabel.setObjectName("OpponentScoreLabel")
        self.PlayerScoreNumber = QtWidgets.QLabel(self.SettingsBox)
        self.PlayerScoreNumber.setGeometry(QtCore.QRect(200, 30, 61, 31))
        self.PlayerScoreNumber.setStyleSheet("border: 2px solid grey;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 900 12pt \"Perpetua Titling MT\";\n"
"color: rgb(0, 0, 0);")
        self.PlayerScoreNumber.setText("")
        self.PlayerScoreNumber.setObjectName("PlayerScoreNumber")
        self.OpponentScoreNumber = QtWidgets.QLabel(self.SettingsBox)
        self.OpponentScoreNumber.setGeometry(QtCore.QRect(200, 80, 61, 31))
        self.OpponentScoreNumber.setStyleSheet("border: 2px solid grey;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 900 12pt \"Perpetua Titling MT\";\n"
"color: rgb(0, 0, 0);")
        self.OpponentScoreNumber.setText("")
        self.OpponentScoreNumber.setObjectName("OpponentScoreNumber")
        self.BetValueNumber = QtWidgets.QLabel(self.SettingsBox)
        self.BetValueNumber.setGeometry(QtCore.QRect(200, 130, 61, 31))
        self.BetValueNumber.setStyleSheet("border: 2px solid grey;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 900 12pt \"Perpetua Titling MT\";\n"
"color: rgb(0, 0, 0);")
        self.BetValueNumber.setText("")
        self.BetValueNumber.setObjectName("BetValueNumber")
        self.ActionsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ActionsBox.setGeometry(QtCore.QRect(480, 620, 351, 141))
        self.ActionsBox.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.ActionsBox.setObjectName("ActionsBox")
        self.PassButton = QtWidgets.QPushButton(self.ActionsBox)
        self.PassButton.setGeometry(QtCore.QRect(30, 50, 75, 51))
        self.PassButton.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"font: 900 12pt \"Perpetua Titling MT\";\n"
"color: rgb(0, 0, 0);")
        self.PassButton.setObjectName("PassButton")
        self.CallButton = QtWidgets.QPushButton(self.ActionsBox)
        self.CallButton.setGeometry(QtCore.QRect(140, 50, 75, 51))
        self.CallButton.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"font: 900 12pt \"Perpetua Titling MT\";\n"
"color: rgb(0, 0, 0);")
        self.CallButton.setObjectName("CallButton")
        self.RaiseButton = QtWidgets.QPushButton(self.ActionsBox)
        self.RaiseButton.setGeometry(QtCore.QRect(250, 50, 71, 51))
        self.RaiseButton.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"font: 900 12pt \"Perpetua Titling MT\";\n"
"color: rgb(0, 0, 0);")
        self.RaiseButton.setObjectName("RaiseButton")
        self.PokerTableImage = QtWidgets.QLabel(self.centralwidget)
        self.PokerTableImage.setGeometry(QtCore.QRect(160, 30, 1001, 871))
        self.PokerTableImage.setText("")
        self.PokerTableImage.setPixmap(QtGui.QPixmap("C:\\Users\\Anton\\PycharmProjects\\course_work\\uis\\../images/Poker_table_picture_full.png"))
        self.PokerTableImage.setObjectName("PokerTableImage")
        self.BoardBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BoardBox.setGeometry(QtCore.QRect(550, 280, 211, 91))
        self.BoardBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(9, 70, 10);")
        self.BoardBox.setObjectName("BoardBox")
        self.card4_board = QtWidgets.QLabel(self.BoardBox)
        self.card4_board.setGeometry(QtCore.QRect(129, 22, 31, 51))
        self.card4_board.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card4_board.setText("")
        self.card4_board.setObjectName("card4_board")
        self.card2_board = QtWidgets.QLabel(self.BoardBox)
        self.card2_board.setGeometry(QtCore.QRect(51, 22, 31, 51))
        self.card2_board.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card2_board.setText("")
        self.card2_board.setObjectName("card2_board")
        self.card3_board = QtWidgets.QLabel(self.BoardBox)
        self.card3_board.setGeometry(QtCore.QRect(90, 22, 31, 51))
        self.card3_board.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card3_board.setText("")
        self.card3_board.setObjectName("card3_board")
        self.card5_board = QtWidgets.QLabel(self.BoardBox)
        self.card5_board.setGeometry(QtCore.QRect(168, 22, 31, 51))
        self.card5_board.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card5_board.setText("")
        self.card5_board.setObjectName("card5_board")
        self.card1_board = QtWidgets.QLabel(self.BoardBox)
        self.card1_board.setGeometry(QtCore.QRect(12, 22, 31, 51))
        self.card1_board.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card1_board.setText("")
        self.card1_board.setObjectName("card1_board")
        self.Hand2Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Hand2Box.setGeometry(QtCore.QRect(610, 190, 91, 81))
        self.Hand2Box.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(9, 70, 10);")
        self.Hand2Box.setObjectName("Hand2Box")
        self.card2_hand2 = QtWidgets.QLabel(self.Hand2Box)
        self.card2_hand2.setGeometry(QtCore.QRect(49, 21, 31, 51))
        self.card2_hand2.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card2_hand2.setText("")
        self.card2_hand2.setObjectName("card2_hand2")
        self.card1_hand2 = QtWidgets.QLabel(self.Hand2Box)
        self.card1_hand2.setGeometry(QtCore.QRect(11, 21, 31, 51))
        self.card1_hand2.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card1_hand2.setText("")
        self.card1_hand2.setObjectName("card1_hand2")
        self.Hand1Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Hand1Box.setGeometry(QtCore.QRect(610, 380, 91, 81))
        self.Hand1Box.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(9, 70, 10);")
        self.Hand1Box.setObjectName("Hand1Box")
        self.card2_hand1 = QtWidgets.QLabel(self.Hand1Box)
        self.card2_hand1.setGeometry(QtCore.QRect(49, 21, 31, 49))
        self.card2_hand1.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"background-color: rgb(0, 0, 98);")
        self.card2_hand1.setText("")
        self.card2_hand1.setObjectName("card2_hand1")
        self.card1_hand1 = QtWidgets.QLabel(self.Hand1Box)
        self.card1_hand1.setGeometry(QtCore.QRect(11, 21, 32, 49))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.card1_hand1.setFont(font)
        self.card1_hand1.setStyleSheet("font: 75 16pt \"Perpetua Titling MT\";\n"
"border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 98);")
        self.card1_hand1.setText("")
        self.card1_hand1.setWordWrap(False)
        self.card1_hand1.setObjectName("card1_hand1")
        self.ReportBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ReportBox.setGeometry(QtCore.QRect(920, 570, 271, 191))
        self.ReportBox.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.ReportBox.setObjectName("ReportBox")
        self.ReportText = QtWidgets.QListWidget(self.ReportBox)
        self.ReportText.setGeometry(QtCore.QRect(20, 30, 231, 141))
        self.ReportText.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"color: rgb(0, 0, 0);")
        self.ReportText.setObjectName("ReportText")
        self.PokerTableImage.raise_()
        self.SettingsBox.raise_()
        self.ActionsBox.raise_()
        self.BoardBox.raise_()
        self.Hand2Box.raise_()
        self.Hand1Box.raise_()
        self.ReportBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setStyleSheet("background-color: rgb(6, 66, 6);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Perpetua Titling MT\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(6, 66, 6);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_game = QtWidgets.QAction(MainWindow)
        self.actionNew_game.setObjectName("actionNew_game")
        self.actionSave_report = QtWidgets.QAction(MainWindow)
        self.actionSave_report.setObjectName("actionSave_report")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionNew_game)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave_report)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SettingsBox.setTitle(_translate("MainWindow", "Game"))
        self.PlayerScoreLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ffffff;\">PLAYER SCORE:</span></p></body></html>"))
        self.BetValueLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ffffff;\">BET value:</span></p></body></html>"))
        self.OpponentScoreLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ffffff;\">OPPONENT SCORE:</span></p></body></html>"))
        self.ActionsBox.setTitle(_translate("MainWindow", "Actions"))
        self.PassButton.setText(_translate("MainWindow", "PASS"))
        self.CallButton.setText(_translate("MainWindow", "CALL"))
        self.RaiseButton.setText(_translate("MainWindow", "RAISE"))
        self.BoardBox.setTitle(_translate("MainWindow", "BOARD"))
        self.Hand2Box.setTitle(_translate("MainWindow", "HAND 2"))
        self.Hand1Box.setTitle(_translate("MainWindow", "HAND 1"))
        self.ReportBox.setTitle(_translate("MainWindow", "Report"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew_game.setText(_translate("MainWindow", "New game"))
        self.actionNew_game.setToolTip(_translate("MainWindow", "This action ends current session and starts new game from the begining"))
        self.actionSave_report.setText(_translate("MainWindow", "Save report"))
        self.actionSave_report.setToolTip(_translate("MainWindow", "This action makes a .txt file with report about current game"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close application"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
