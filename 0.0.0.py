# -*- coding: utf-8 -*-
import sqlite3
import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

import creation_window
from PyQt5.QtWidgets import QApplication, QMainWindow
from test_maket import Ui_MainWindow
from db_only import deleting_identical_notes


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crbt_notes.clicked.connect(self.open_second_form)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        # self..clicked.connect(self.)
        self.deletebt_notes.clicked.connect(self.delete_data_listwidget)
        self.refresh.clicked.connect(self.deleting_identical_notes_call)

    @staticmethod
    def open_second_form():
        creation_window.main()

    def deleting_identical_notes_call(self):
        deleting_identical_notes()

    def filling_data_listwidget(self):
        """сделать автоматическое удаление одинаковых записей"""
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db = cur.execute(f"SELECT data FROM Data").fetchall()
        self.listWidget.clear()
        for data in db:
            self.listWidget.addItems(data)
        # con.commit()
        # con.close()

    def delete_data_listwidget(self):
        # надо узнать id элемента из бд
        id = self.listWidget.currentRow()
        print(id)
        print(self.listWidget.currentItem().text())

        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        cur.execute("DELETE FROM Data WHERE id = ?", (id,))
        con.commit()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
