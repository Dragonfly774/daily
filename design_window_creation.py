# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_window_creation.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 314)
        MainWindow.setStyleSheet("background-color: #40E0D0 ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: #bc8f8f")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.comboBox_choice = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_choice.setStyleSheet("background-color: #fffff\n"
"color: #0047AB\n"
"\n"
"")
        self.comboBox_choice.setObjectName("comboBox_choice")
        self.gridLayout.addWidget(self.comboBox_choice, 0, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("background-color: #ffffff")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Создание записи"))
        self.pushButton_2.setText(_translate("MainWindow", "сохранить"))
        self.label.setText(_translate("MainWindow", "           категория >"))
