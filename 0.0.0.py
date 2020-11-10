# -*- coding: utf-8 -*-
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
        self.refresh.clicked.connect(self.showing_tableview)

    @staticmethod
    def open_second_form():
        creation_window.main()

    def showing_tableview(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('project_db.db')
        db.open()
        view = self.tableView
        model = QSqlTableModel(self, db)
        model.setTable('Data')
        model.select()
        view.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
