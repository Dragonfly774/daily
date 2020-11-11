# -*- coding: utf-8 -*-
import sys
import sqlite3
import datetime as dt
from PyQt5.QtWidgets import QApplication, QMainWindow
from design_window_creation import Ui_MainWindow_cr
from db_only import deleting_identical_notes

category = {1: 'нет', 2: 'цели', 3: 'сегодня', 4: 'важное', 5: 'встреча'}


class MyWidget(QMainWindow, Ui_MainWindow_cr):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_choice.addItems([category[1], category[2], category[3], category[4], category[5]])
        self.pushButton_2.clicked.connect(self.save_psh)

    def save_psh(self):
        self.saving_notes_to_database()

    def saving_notes_to_database(self):
        """сохранение заметки в базу данных"""
        info = self.textEdit.toPlainText()
        value_combobox = self.comboBox_choice.currentText()
        for i, j in category.items():
            if value_combobox == category.get(i):
                value_combobox = i

        if info:
            con = sqlite3.connect('project_db.db')
            cur = con.cursor()
            datetime = dt.datetime.now()

            cur.execute(f"INSERT INTO Data(section, data, datetime, category) VALUES(1, ?, ?, ?)",
                        (info, datetime, value_combobox)).fetchall()
            con.commit()
            con.close()



def main():
    global ex_2
    ex_2 = MyWidget()
    ex_2.show()
    # deleting_identical_notes()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWidget()
#     ex.show()
#     sys.exit(app.exec_())
