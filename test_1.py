from PyQt5 import Qt


class Tab(Qt.QTabWidget):
    def __init__(self):
        Qt.QTabWidget.__init__(self)
        self.addTab(Qt.QTextEdit(), "edit1")
        self.addTab(Qt.QTextEdit(), "edit2")
        self.currentChanged.connect(self.on_tab)

    def on_tab(self):
        print(self.currentIndex())


if __name__ == "__main__":
    app = Qt.QApplication([])
    t = Tab()
    t.show()
    app.exec_()
