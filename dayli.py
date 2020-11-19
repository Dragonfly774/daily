# -*- coding: utf-8 -*-
import sqlite3
import sys
import creation_window
from edit import editing_window_note
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from db_only import deleting_identical_notes


# from test_calendar import main


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crbt_notes.clicked.connect(self.open_second_form)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        self.deletebt_notes.clicked.connect(self.delete_data_listwidget)
        self.deletebt_notes.clicked.connect(self.deleting_identical_notes_call)
        self.refresh.clicked.connect(self.deleting_identical_notes_call)
        self.deletebt_notes.clicked.connect(self.filling_data_listwidget)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        self.data_list = ''
        self.dates_calendar = {}
        self.pushButton.clicked.connect(self.find_date)
        # self.listWidget.itemClicked.connect(self.editing_a_note)  # вызов окно редактирование и просмотра по нажатию

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
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db = cur.execute(f"SELECT data FROM Data").fetchall()
        # self.listWidget.clear()
        # print(db)
        # db = cur.execute(f"SELECT data, category FROM Data").fetchall()
        # print(db)
        self.listWidget.clear()
        for data in db:
            self.listWidget.addItems(data)
        self.listWidget.itemDoubleClicked.connect(self.editing_a_note)
        self.filling_data_listwidget
        # db_data = []
        # db_data_list = []
        # for i in range(len(db)):
        #     db_data.append(db[i][0])
        # print(db_data)
        # for k in db_data:
        #     db_data_list.append(tuple(k))
        # for j in db_data:
        #     self.listWidget.addItems(tuple(j))

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


    def find_date(self):
        """календарь, создание заметки"""
        # получаем дату
        string_date = self.calendarWidget.selectedDate().getDate()
        # добавляем ноль, елси месяц <= 9
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        # добавляем ноль, елси день <= 9
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        line_edit = self.lineEdit.text()
        # задаем словарю новое значения
        self.dates_calendar[
            f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}'] = line_edit
        self.textBrowser.clear()
        # сортируем даты и выводим их
        for key in sorted(self.dates_calendar.keys()):
            self.textBrowser.append(f'{key} - {self.dates_calendar[key]}')

        self.save_to_calendar(line_edit, string_date)

    def save_to_calendar(self, line_edit, string_date):
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        cur.execute(f"INSERT INTO calendar (section, data, datetime) VALUES(3, ?, ?)",
                    (line_edit, string_date)).fetchall()
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
