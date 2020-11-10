from test_maket import Ui_MainWindow

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class ShowT(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_table(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('project_db.db')
        db.open()
        view = self.tableView
        model = QSqlTableModel(self, db)
        model.setTable('data')
        model.select()
        view.setModel(model)


def main():
    global ex_3
    ex_3 = ShowT()
