import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from edit_window import Ui_EditWindow_E


class Edit(Ui_EditWindow_E, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        data_text_listwidget = self.test_maket.Ui_MainWindow.setupUi.listWidget.currentItem().text()
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        data_edit = self.textEdit.toPlainText()
        cur.execute(f"UPDATE Data SET data = ? WHERE data = ?", (data_edit, str(data_text_listwidget))).fetchall()
        con.commit()
        con.close()


def main():
    global ex
    #  Edit.run(data_text_listwidget)
    ex = Edit()
    ex.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Edit()
#     ex.show()
#     sys.exit(app.exec_())