import sqlite3
import datetime as dt
from PyQt5.QtWidgets import QApplication, QMainWindow
from design_window_calendar import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, string_date):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save_psh)
        self.string_date = string_date

    def save_psh(self):
        self.saving_notes_to_database()

    def saving_notes_to_database(self):
        """сохранение заметки в базу данных"""
        info = self.textEdit.toPlainText()

        if info:
            con = sqlite3.connect('project_db.db')
            cur = con.cursor()

            cur.execute(f"INSERT INTO calendar(section, data, datetime) VALUES(3, ?, ?)",
                        (info, str(self.string_date))).fetchall()
            con.commit()
            con.close()
        print(self.string_date)


def main(string_date):
    global ex_2
    ex_2 = MyWidget(string_date)
    ex_2.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWidget()
#     ex.show()
#     sys.exit(app.exec_())
