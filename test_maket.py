# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_maket.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.crbt_notes = QtWidgets.QPushButton(self.tab)
        self.crbt_notes.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.crbt_notes.setMinimumSize(QtCore.QSize(21, 0))
        self.crbt_notes.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.crbt_notes.setObjectName("crbt_notes")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.crbt_tasks = QtWidgets.QPushButton(self.tab_2)
        self.crbt_tasks.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.crbt_tasks.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.crbt_tasks.setObjectName("crbt_tasks")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget.setStyleSheet("alternate-background-color: rgb(85, 255, 127);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.calendarWidget)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.crbt_notes.setText(_translate("MainWindow", "+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Заметки"))
        self.crbt_tasks.setText(_translate("MainWindow", "+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Задачи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Календарь"))
