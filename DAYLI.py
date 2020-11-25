# -*- coding: utf-8 -*-
import sqlite3
import sys

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QTextCharFormat, QColor

import creation_window
import creation_window_calendar
from edit import editing_window_note
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from db_only import deleting_identical_notes, deleting_identical_calendar

category = [(1, 'нет'), (2, 'цели'), (3, 'сегодня'), (4, 'важное'), (5, 'встреча')]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        """заметки"""

        self.crbt_notes.clicked.connect(self.open_second_form)
        self.deletebt_notes.clicked.connect(self.delete_data_listwidget)
        self.deletebt_notes.clicked.connect(self.deleting_identical_notes_call)
        self.refresh.clicked.connect(self.deleting_identical_notes_call)
        self.deletebt_notes.clicked.connect(self.filling_data_listwidget)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        self.filling_data_listwidget()
        self.data_list = ''
        self.deleting_identical_notes_call()
        self.all_dates = {}

        """календарь"""

        self.string_date = 0
        self.pushButton.clicked.connect(self.creation_find_date)
        self.pushButton_2.clicked.connect(self.filling_data_listwidget_calendar)
        self.pushButton_3.clicked.connect(self.delete_data_listwidget_calendar)
        self.pushButton_3.clicked.connect(self.filling_data_listwidget_calendar)
        self.pushButton_3.clicked.connect(self.deleting_identical_calendar_call)
        self.filling_data_listwidget_calendar()
        self.deleting_identical_calendar_call()

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
        try:
            self.data_list = self.listWidget.currentItem().text()
            editing_window_note.main(self.data_list)
            self.filling_data_listwidget()
        except AttributeError:
            pass

    def filling_data_listwidget(self):
        """заполнение из бд в listWidget
        """
        self.listWidget.clear()
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
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
        try:
            data_text_listwidget_del = self.listWidget.currentItem().text()
            data = list(map(lambda x: x[0], data))
            for i in range(len(data)):
                if data[i] == data_text_listwidget_del:
                    con1 = sqlite3.connect('project_db.db')
                    cur1 = con1.cursor()
                    cur1.execute("DELETE FROM Data WHERE data = ?", (data_text_listwidget_del,))
                    con1.commit()
                    con1.close()
        except AttributeError:
            pass

    """-----------------------------Календарь-----------------------------"""

    def creation_find_date(self):
        """вызов функции из 'creation_window_calendar.py', которая создает заметки и сохраняет
        эта функиция еще берет данные времени и передает их в "creation_window_calendar.py"
        """
        self.string_date = self.calendarWidget.selectedDate().getDate()

        if int(self.string_date[1]) <= 9:
            self.string_date = (self.string_date[0], '0' + str(self.string_date[1]), self.string_date[-1])

        if int(self.string_date[2]) <= 9:
            self.string_date = (self.string_date[0], str(self.string_date[1]), '0' + str(self.string_date[-1]))
        creation_window_calendar.main(self.string_date)
        self.deleting_identical_calendar_call()

    def filling_data_listwidget_calendar(self):
        """заполнение из бд в listWidget для календаря"""
        deleting_identical_calendar()
        self.listWidget_3.clear()
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db_data = cur.execute(f"SELECT data FROM calendar").fetchall()
        db_datetime = cur.execute(f"SELECT data, datetime FROM calendar").fetchall()
        db_data_list = []
        db_datetime_list = []
        for i in db_data:
            db_data_list.append(i)
        for j in db_datetime:
            db_datetime_list.append(j)
        db_data_list = list(map(lambda x: x[0], db_data_list))
        db_datetime_list = list(map(lambda x: x[1], db_datetime_list))
        self.listWidget.clear()
        for i in range(len(db_data_list)):
            if self.calendarWidget.selectedDate().getDate() == eval(db_datetime_list[i]):
                self.listWidget_3.addItem(db_data_list[i])
        color = '#1faee9'
        self.color_change(db_datetime_list, db_data_list, color)
        self.listWidget_3.itemDoubleClicked.connect(self.editing_a_calendar)
        deleting_identical_calendar()

    def color_change(self, db_datetime_list, db_data_list, color):
        test = [tuple(i.strip(")").strip("(").split(", ")) for i in db_datetime_list]
        for i in range(len(db_data_list)):
            format = QTextCharFormat()

            format.setBackground(QColor(color))
            self.calendarWidget.setDateTextFormat(QDate(int(test[i][0]), int(test[i][1]), int(test[i][2])), format)

        self.listWidget_3.itemDoubleClicked.connect(self.editing_a_calendar)
        deleting_identical_calendar()

    def editing_a_calendar(self):
        """вызов окна редактирования в календаре"""
        self.data_list = self.listWidget_3.currentItem().text()
        editing_window_note.main_calendar(self.data_list)

    @staticmethod
    def deleting_identical_calendar_call():
        """вызов функции из 'db_only.py', которая удалит одиннаковые замекти в календаре"""
        deleting_identical_calendar()

    def delete_data_listwidget_calendar(self):
        """удаление выбранной заметки в календаре"""
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        result = cur.execute("SELECT data FROM calendar")
        # db_datetime = cur.execute(f"SELECT datetime FROM calendar").fetchone()
        data = []
        for i in result:
            data.append(i)
        try:
            data_text_listwidget_del = self.listWidget_3.currentItem().text()
            data = list(map(lambda x: x[0], data))
            # data_1 = list(map(lambda x: x[0], data))
            for i in range(len(data)):
                if data[i] == data_text_listwidget_del:
                    con1 = sqlite3.connect('project_db.db')
                    cur1 = con1.cursor()
                    cur1.execute("DELETE FROM calendar WHERE data = ?", (data_text_listwidget_del,))
                    con1.commit()
                    con1.close()

        except AttributeError:
            pass
        # self.color_change_back(data_1, db_datetime)

    # def color_change_back(self, data, db_datetime):
    #     print(db_datetime)
    #     db_datetime_list = []
    #     for j in db_datetime:
    #         db_datetime_list.append(j)
    #     print(db_datetime_list)
    #     db_datetime_list = list(map(lambda x: x, db_datetime_list))
    #     print(db_datetime_list)
    #     test = [tuple(i.strip(")").strip("(").split(", ")) for i in db_datetime_list]
    #     print('test', test)
    #     for i in range(len(data)):
    #         format = QTextCharFormat()
    #         format.setBackground(QColor('#40E0D1'))
    #         self.calendarWidget.setDateTextFormat(QDate(int(test[i][0]), int(test[i][1]), int(test[i][2])), format)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
