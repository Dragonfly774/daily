# -*- coding: utf-8 -*-
import sys
import sqlite3
import datetime as dt
from PyQt5.QtWidgets import QApplication, QMainWindow
from design_window_creation import Ui_MainWindow_cr

category = {1: 'встреча', 2: 'цели', 3: 'сегодня', 4: 'важное', 5: 'нет'}


class MyWidget(QMainWindow, Ui_MainWindow_cr):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_choice.addItems([category[1], category[2], category[3], category[4], category[5]])
        self.pushButton_2.clicked.connect(self.save_psh)

    def save_psh(self):
        self.saving_notes_to_database()

    def saving_notes_to_database(self):
        info = self.textEdit.toPlainText()
        value_comboBox = self.comboBox_choice.currentText()
        for i, j in category.items():
            if value_comboBox == category.get(i):
                value_comboBox = i
        if info:
            con = sqlite3.connect('project_db.db')
            cur = con.cursor()
            datetime = dt.datetime.now()
            cur.execute(f"INSERT INTO Data(section, data, datetime, category) VALUES(1, ?, ?, ?)",
                        (info, datetime, value_comboBox)).fetchall()
            con.commit()
            con.close()


# def main():
#     global ex_2
#     ex_2 = MyWidget()
#     ex_2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
