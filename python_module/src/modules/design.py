#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


try:
    # Включите в блок try/except, если вы также нацелены на Mac/Linux
    from PyQt5.QtWinExtras import QtWin                                         #  !!!
    myappid = 'mycompany.myproduct.subproduct.version'                          #  !!!
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)                      #  !!!
except ImportError:
    pass


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon('icon.png'))

        window = QtWidgets.QWidget()
        window.setWindowIcon(QtGui.QIcon('icon.png'))
        window.show()

    def initUI(self):

        receiver = QLabel('Получатель')
        author = QLabel('Тема')
        review = QLabel('Сообщение')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        quit_btn = QPushButton('Выйти', self)
        quit_btn.clicked.connect(QApplication.instance().quit)

        receiver_edit = QLineEdit()
        theme_edit = QLineEdit()
        message_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(receiver, 1, 0)
        grid.addWidget(receiver_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(theme_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(message_edit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(450, 450, 500, 450)
        self.setWindowTitle('Tremolo - Отправить сообщение')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
