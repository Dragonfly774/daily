# -*- coding: utf-8 -*-
import sqlite3
import sys

import creation_window
from PyQt5.QtWidgets import QApplication, QMainWindow
from test_maket import Ui_MainWindow
from db_only import deleting_identical_notes

global d


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crbt_notes.clicked.connect(self.open_second_form)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        # self..clicked.connect(self.)
        self.deletebt_notes.clicked.connect(self.delete_data_listwidget)
        self.refresh.clicked.connect(self.deleting_identical_notes_call)
        self.editi.clicked.connect(self.editing_a_note)
    @staticmethod
    def open_second_form():
        """вызов функции из 'creation_window.py', которая создает заметки"""
        creation_window.main()

    @staticmethod
    def deleting_identical_notes_call():
        """вызов функции из 'db_only.py', которая удалит одиннаковые замекти"""
        deleting_identical_notes()

    def filling_data_listwidget(self):
        """заполнение из бд в listWidget"""
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db = cur.execute(f"SELECT data FROM Data").fetchall()
        self.listWidget.clear()
        for data in db:
            self.listWidget.addItems(data)

    def delete_data_listwidget(self):
        """удаление выбранной заметки"""
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        result = cur.execute("SELECT data FROM Data")
        data = []
        for i in result:
            data.append(i)
        data_text_listwidget_del = self.listWidget.currentItem().text()
        data = list(map(lambda x: x[0], data))
        for i in range(len(data)):
            if data[i] == data_text_listwidget_del:
                con1 = sqlite3.connect('project_db.db')
                cur1 = con1.cursor()
                cur1.execute("DELETE FROM Data WHERE data = ?", (data_text_listwidget_del,))
                con1.commit()
                con1.close()

    def editing_a_note(self):
        # d = []
        # d = self.listWidget.currentItem().text()

        creation_window.main()
        creation_window.main_edit()
        # data_text_listwidget = self.listWidget.currentItem().text()
        # con = sqlite3.connect('project_db.db')
        # cur = con.cursor()
        # result = cur.execute("SELECT data FROM Data")
        # data = []
        # data = [data.append(i) for i in result]
        # creation_window.main()
        # print(str(creation_window.MyWidget.run))
        # for i in range(len(data)):
        #     if data[i] == data_text_listwidget:
        #
        #         con1 = sqlite3.connect('project_db.db')
        #         cur1 = con1.cursor()
        #         cur1.execute(f"UPDATE Data SET data = ? WHERE data = ?",
        #                      (str(creation_window.MyWidget.run), str(data_text_listwidget)))
        #         con1.commit()
        #         con1.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
