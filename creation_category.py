import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from category_creation_window import Ui_MainWindow

category = {1: 'нет', 2: 'цели', 3: 'сегодня', 4: 'важное', 5: 'встреча', 6: 'своя'}


class Category(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems([category[1], category[2], category[3], category[4], category[5], category[6]])
        self.pushButton.clicked.connect(self.run)

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Category()
    ex.show()
    sys.exit(app.exec_())

# def main():
#     global ex
#     ex = Category()
#     ex.show()