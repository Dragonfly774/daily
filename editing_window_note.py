import sqlite3
import sys
# from dayli import MyWidget
import dayli
from PyQt5.QtWidgets import QMainWindow, QApplication

from edit_window import Ui_EditWindow_E


class Edit(Ui_EditWindow_E, QMainWindow):
    def __init__(self, data_del):
        super().__init__()
        self.setupUi(self)
        self.data_del = data_del
        self.pushButton.clicked.connect(self.run)

    def run(self):
        data = self.textEdit.toPlainText()
        print(str(data))
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        result = cur.execute("SELECT data FROM Data")
        data_edit = []
        for i in result:
            data_edit.append(i)
        data_edit = list(map(lambda x: x[0], data_edit))
        print(data_edit)
        print(self.data_del)
        for i in range(len(data_edit)):
            if data_edit[i] == self.data_del:
                con1 = sqlite3.connect('project_db.db')
                cur1 = con1.cursor()
                cur1.execute(f"UPDATE Data SET data = ? WHERE data = ?", (str(data), self.data_del))
                con1.commit()
                con1.close()


def main(data_del):
    global ex
    ex = Edit(data_del)
    ex.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Edit()
#     ex.show()
#     sys.exit(app.exec_())