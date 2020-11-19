import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication

from edit.edit_window import Ui_EditWindow


class Edit(Ui_EditWindow, QMainWindow):
    def __init__(self, data_del):
        super().__init__()
        self.setupUi(self)
        self.data_del = data_del
        self.pushButton.clicked.connect(self.run)
        self.textEdit.setText(self.data_del)

    def run(self):
        """
        редактирование data в заметках
        """
        data = self.textEdit.toPlainText()
        con = sqlite3.connect('project_db.db')
        cur = con.cursor()
        result = cur.execute("SELECT data FROM Data")
        data_edit = []
        for i in result:
            data_edit.append(i)
        data_edit = list(map(lambda x: x[0], data_edit))
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
