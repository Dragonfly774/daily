# -*- coding: utf-8 -*-
import sqlite3
import sys

import creation_window
import editing_window_note
# from edit_window import Ui_EditWindow_E  # из edit_window
from PyQt5.QtWidgets import QApplication, QMainWindow
from test_maket import Ui_MainWindow
from db_only import deleting_identical_notes



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crbt_notes.clicked.connect(self.open_second_form)
        self.refresh.clicked.connect(self.filling_data_listwidget)
        self.deletebt_notes.clicked.connect(self.delete_data_listwidget)
        self.refresh.clicked.connect(self.deleting_identical_notes_call)
        self.editi.clicked.connect(self.editing_a_note)
        self.data_list = ''
        # self.data_list = self.listWidget.currentItem().text()


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
        self.data_list = self.listWidget.currentItem().text()
        editing_window_note.main(self.data_list)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

# class Edit(Ui_EditWindow_E, QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.run)
#
#     def run(self):
#         data = self.textEdit.toPlainText()
#         print(str(data))
#         con = sqlite3.connect('project_db.db')
#         cur = con.cursor()
#         result = cur.execute("SELECT data FROM Data")
#         data_edit = []
#         data_edit = [data_edit.append(i) for i in result]
#         data_del = data_list
#         print(data_del)
#         for i in range(len(data_edit)):
#             if data_edit[i] == data_del:
#                 con1 = sqlite3.connect('project_db.db')
#                 cur1 = con1.cursor()
#                 cur1.execute(f"UPDATE Data SET data = ? WHERE data = ?", (data, data_del))
#                 con1.commit()
#                 con1.close()

# def main():
#     global ex
#     ex = Edit()
#     ex.show()