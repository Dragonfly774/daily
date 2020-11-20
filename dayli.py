# -*- coding: utf-8 -*-
import sqlite3
import sys
import creation_window
from edit import editing_window_note
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from db_only import deleting_identical_notes


category = [(1, 'нет'), (2, 'цели'), (3, 'сегодня'), (4, 'важное'), (5, 'встреча')]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crbt_notes.clicked.connect(self.open_second_form)
        self.deletebt_notes.clicked.connect(self.delete_data_listwidget)
        self.deletebt_notes.clicked.connect(self.deleting_identical_notes_call)
        self.refresh.clicked.connect(self.deleting_identical_notes_call)
        self.deletebt_notes.clicked.connect(self.filling_data_listwidget)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        self.data_list = ''
        self.deleting_identical_notes_call()

    @staticmethod
    def open_second_form():
        """вызов функции из 'creation_window.py', которая создает заметки"""
        creation_window.main()

    @staticmethod
    def deleting_identical_notes_call():
        """вызов функции из 'db_only.py', которая удалит одиннаковые замекти"""
        deleting_identical_notes()

    def editing_a_note(self):
        """вызов окна редактирования"""
        self.data_list = self.listWidget.currentItem().text()
        editing_window_note.main(self.data_list)

    def filling_data_listwidget(self):
        """заполнение из бд в listWidget
        """
        self.listWidget.clear()
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db = cur.execute(f"SELECT data FROM Data").fetchall()
        db_category = cur.execute(f"SELECT data, category FROM Data").fetchall()
        data_category = []
        s = []
        for k in db_category:
            s.append(k)

        for i in range(len(s)):
            data_category.append(db_category[i][1])

        s1, s2, s3, s4, s5 = [], [], [], [], []
        for i in range(len(db_category)):
            if db_category[i][1] == 1:
                s1.append(db_category[i][0])
            if db_category[i][1] == 2:
                s2.append(db_category[i][0])
            if db_category[i][1] == 3:
                s3.append(db_category[i][0])
            if db_category[i][1] == 4:
                s4.append(db_category[i][0])
            if db_category[i][1] == 5:
                s5.append(db_category[i][0])

        if s1:
            for i in s1:
                self.listWidget.addItem(i)
            separator = "-------------------------------"
            self.listWidget.addItem(separator)

        if s2:
            past = f'{category[1][1]}:'
            self.listWidget.addItem(past)
            for i in s2:
                self.listWidget.addItem(i)
            separator = "-------------------------------"
            self.listWidget.addItem(separator)

        if s3:
            past = f'{category[2][1]}:'
            self.listWidget.addItem(past)
            for i in s3:
                self.listWidget.addItem(i)
            separator = "-------------------------------"
            self.listWidget.addItem(separator)

        if s4:
            past = f'{category[3][1]}:'
            self.listWidget.addItem(past)
            for i in s4:
                self.listWidget.addItem(i)
            separator = "-------------------------------"
            self.listWidget.addItem(separator)

        if s5:
            past = f'{category[4][1]}:'
            self.listWidget.addItem(past)
            for i in s5:
                self.listWidget.addItem(i)
            separator = "-------------------------------"
            self.listWidget.addItem(separator)

        self.listWidget.itemDoubleClicked.connect(self.editing_a_note)

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



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
