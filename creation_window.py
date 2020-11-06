# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from design_window_creation import Ui_MainWindow_cr


class MyWidget(QMainWindow, Ui_MainWindow_cr):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ryn)

    def ryn(self):
        s = self.lineEdit.text()
        self.lineEdit_2.setText(s)


# if __name__ == '__main__':
def main():
    global ex
    ex = MyWidget()
    ex.show()


