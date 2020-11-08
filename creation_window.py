# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design_window_creation import Ui_MainWindow_cr
from main import save_notes_data


class MyWidget(QMainWindow, Ui_MainWindow_cr):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save_psh)
        # self.pushButton_2.clicked.connect(self.save_psh)

    def save_psh(self):
        self.saving_notes_to_database()

    def saving_notes_to_database(self):
        info = self.textEdit.toPlainText()
        print(info)
        self.lineEdit.setText(info)
        if info:
            save_notes_data(info)


# def main():
#     global ex_2
#     ex_2 = MyWidget()
#     ex_2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
