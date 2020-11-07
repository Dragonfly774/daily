# -*- coding: utf-8 -*-
import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow

import creation_window
from test_maket import Ui_MainWindow
from design_window_creation import Ui_MainWindow_cr


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.crbt_notes.clicked.connect(self.open_second_form)

    @staticmethod
    def open_second_form():
        creation_window.main()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
