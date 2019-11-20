import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

import uis.poker_gui


class MainWindow(QtWidgets.QMainWindow, uis.poker_gui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле poker_gui.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего интерфейса


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.card1_hand1.setText("Q♠")
    window.show()  # Показываем окно

    app.exec_()  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
