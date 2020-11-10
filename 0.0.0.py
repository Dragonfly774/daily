# -*- coding: utf-8 -*-
import sqlite3
import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

import creation_window
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from test_maket import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crbt_notes.clicked.connect(self.open_second_form)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        # self..clicked.connect(self.)
        self.deletebt_notes.clicked.connect(self.delete_data_listwidget)


    @staticmethod
    def open_second_form():
        creation_window.main()

    def filling_data_listwidget(self):
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db = cur.execute(f"SELECT data FROM Data").fetchall()
        for data in db:
            self.listWidget.addItems(data)
        # con.commit()
        # con.close()

    def delete_data_listwidget(self):
        id = self.listWidget.currentRow()
        print(self.listWidget.currentItem().text())
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db = cur.execute(f"DELETE FROM Data WHERE data = {id - 1}").fetchall()
        con.commit()
        con.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
