import sqlite3
import sys
import creation_window_calendar
from PyQt5.QtWidgets import QApplication, QMainWindow

from edit import editing_window_note
from main_window import Ui_MainWindow
from db_only import deleting_identical_calendar


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.all_dates = {}
        self.string_date = 0
        self.pushButton.clicked.connect(self.creation_find_date)
        self.pushButton_2.clicked.connect(self.filling_data_listwidget)
        # self.deleting_identical_calendar_call()

    def creation_find_date(self):
        """вызов функции из 'creation_window_calendar.py', которая создает заметки и сохраняет
        эта функиция еще берет данные времени и передает их в "creation_window_calendar.py"
        """
        # получаем дату
        self.string_date = self.calendarWidget.selectedDate().getDate()
        # добавляем ноль, елси месяц <= 9
        if int(self.string_date[1]) <= 9:
            string_date = (self.string_date[0], '0' + str(self.string_date[1]), self.string_date[-1])
        # добавляем ноль, елси день <= 9
        if int(self.string_date[2]) <= 9:
            self.string_date = (self.string_date[0], str(self.string_date[1]), '0' + str(self.string_date[-1]))
        creation_window_calendar.main(self.string_date)

    def filling_data_listwidget(self):
        """заполнение из бд в listWidget"""
        self.listWidget_3.clear()
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        db_data = cur.execute(f"SELECT data FROM calendar").fetchall()
        db_datetime = cur.execute(f"SELECT data, datetime FROM calendar").fetchall()
        print(db_data)
        print(db_datetime)
        db_data_list = []
        db_datetime_list = []
        for i in db_data:
            db_data_list.append(i)
        for j in db_datetime:
            db_datetime_list.append(j)
        print(self.calendarWidget.selectedDate().getDate())
        db_data_list = list(map(lambda x: x[0], db_data_list))
        db_datetime_list = list(map(lambda x: x[1], db_datetime_list))
        print(db_datetime_list)
        print(db_data_list)
        self.listWidget.clear()
        for i in range(len(db_data_list)):
            if self.calendarWidget.selectedDate().getDate() == eval(db_datetime_list[i]):
                self.listWidget_3.addItem(db_data_list[i])

        # self.listWidget.addItem()
        self.listWidget_3.itemDoubleClicked.connect(self.editing_a_note)
        """вызов функции из 'db_only.py', которая удалит одиннаковые замекти"""
        deleting_identical_calendar()

    # def editing_a_note(self):
    #     """вызов окна редактирования"""
    #     # self.data_list = self.listWidget.currentItem().text()
    #     editing_window_note.main()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

# def main():
#     global ex
#     ex = Example()
#     ex.show()
