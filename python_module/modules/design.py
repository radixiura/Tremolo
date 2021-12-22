#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        receiver = QLabel('Получатель')
        author = QLabel('Тема')
        review = QLabel('Сообщение')

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

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
