import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget

# from button import Ui_MainWindow
#
#
# class MyWidget(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.run)
#
#     def run(self):
#         print(-123)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWidget()
#     ex.show()
#     sys.exit(app.exec_())
from PyQt5.uic.properties import QtWidgets

rows = [
    {'text': 'Row1', 'value': 1, 'group': 1},
    {'text': 'Row2', 'value': 2, 'group': 1},
    {'text': 'Row3', 'value': 3, 'group': 1},
    {'text': 'Row4', 'value': 4, 'group': 2},
    {'text': 'Row5', 'value': 5, 'group': 2},
    {'text': 'Row6', 'value': 6, 'group': 3},
    {'text': 'Row7', 'value': 7, 'group': 3},
    {'text': 'Row8', 'value': 8, 'group': 3},
    {'text': 'Row9', 'value': 9, 'group': 2},
    {'text': 'Row10', 'value': 10, 'group': 'testing'}
]

grouptitles = [1, 2, 3, 'testing']  # list of grouptitles


def gruppe(d):  # function for sorting the itemlist
    return str(d['group'])


rows.sort(key=gruppe, reverse=False)  # sort rows by groups


class MyList(QtWidgets):
    def __init__(self):
        QtWidgets.QListWidget.__init__(self)
        self.setMinimumHeight(270)
        for t in grouptitles:
            item = QtWidgets.QListWidgetItem('Group {}'.format(t))
            item.setData(33, 'header')
            item.setData(34, t)
            item.setFlags(QtWidgets.Qt.ItemIsEnabled | QtWidgets.Qt.ItemIsSelectable)
            self.addItem(item)
            for row in rows:
                if row['group'] == t:
                    item = QtWidgets.QListWidgetItem(row['text'])
                    # These are utilizing the ItemDataRole; 33 and 34 are among the first user defined values
                    # http://pyqt.sourceforge.net/Docs/PyQt4/qt.html#ItemDataRole-enum
                    item.setData(33, row['value'])
                    item.setData(34, row['group'])
                    item.setFlags(
                        QtWidgets.QtCore.Qt.ItemIsUserCheckable | QtWidgets.QtCore.Qt.ItemIsEnabled | QtWidgets.Qt.ItemIsSelectable)
                    item.setCheckState(QtWidgets.QtCore.Qt.Unchecked)
                    self.addItem(item)
                else:
                    pass

        self.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)  #
        self.itemClicked.connect(self.selManager)  # select an appropriate signal

    def selManager(self, item):
        if item.data(33) == 'header':
            groupcode = item.data(34)
            for i in range(0, self.count()):
                if self.item(i).data(34) == groupcode and self.item(i).data(33) != 'header':
                    b = True if self.item(i).isSelected() == False else False
                    self.item(i).setSelected(b)
        else:
            if item.checkState() == QtWidgets.Qt.Unchecked:
                item.setCheckState(QtWidgets.Qt.Checked)
                self.moveItem(self.currentRow(), 0)
            else:
                item.setCheckState(QtWidgets.Qt.Unchecked)
                text = 'Group {}'.format(item.data(34))
                new = self.indexFromItem(
                    self.findItems(text, QtWidgets.Qt.MatchExactly)[0]).row()  # find the row of the headeritem
                self.moveItem(self.currentRow(), new)  # moving back to group

    def moveItem(self, old, new):  # from row(old) to row(new)
        ni = self.takeItem(old)
        self.insertItem(new, ni)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_list = MyList()
    my_list.show()
    sys.exit(app.exec_())
