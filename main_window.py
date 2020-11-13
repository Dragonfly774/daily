# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: #40E0D1")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.crbt_notes = QtWidgets.QPushButton(self.tab)
        self.crbt_notes.setMinimumSize(QtCore.QSize(21, 0))
        self.crbt_notes.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.crbt_notes.setObjectName("crbt_notes")
        self.gridLayout_3.addWidget(self.crbt_notes, 0, 0, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.tab)
        self.refresh.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.refresh.setObjectName("refresh")
        self.gridLayout_3.addWidget(self.refresh, 0, 1, 1, 1)
        self.deletebt_notes = QtWidgets.QPushButton(self.tab)
        self.deletebt_notes.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;\n"
"")
        self.deletebt_notes.setObjectName("deletebt_notes")
        self.gridLayout_3.addWidget(self.deletebt_notes, 0, 2, 1, 1)
        self.editi = QtWidgets.QPushButton(self.tab)
        self.editi.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.editi.setObjectName("editi")
        self.gridLayout_3.addWidget(self.editi, 0, 3, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setStyleSheet("background-color: #FFFfff")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 1, 0, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.crbt_tasks = QtWidgets.QPushButton(self.tab_2)
        self.crbt_tasks.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b6;\n"
"text-align: center;\n"
"border-radius: 6px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.crbt_tasks.setObjectName("crbt_tasks")
        self.gridLayout_4.addWidget(self.crbt_tasks, 0, 0, 1, 1)
        self.refresh_2 = QtWidgets.QPushButton(self.tab_2)
        self.refresh_2.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.refresh_2.setObjectName("refresh_2")
        self.gridLayout_4.addWidget(self.refresh_2, 0, 1, 1, 1)
        self.deletebt_notes_2 = QtWidgets.QPushButton(self.tab_2)
        self.deletebt_notes_2.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;\n"
"")
        self.deletebt_notes_2.setObjectName("deletebt_notes_2")
        self.gridLayout_4.addWidget(self.deletebt_notes_2, 0, 2, 1, 1)
        self.editi_2 = QtWidgets.QPushButton(self.tab_2)
        self.editi_2.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.editi_2.setObjectName("editi_2")
        self.gridLayout_4.addWidget(self.editi_2, 0, 3, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setStyleSheet("background-color: #FFFfff")
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_4.addWidget(self.listWidget_2, 1, 0, 1, 4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_3)
        self.timeEdit.setStyleSheet("background-color: #bc8f8f")
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_2.addWidget(self.timeEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setStyleSheet("color: #ff9218;\n"
"background-color: #ffe5b9;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 130px;\n"
"height: 30px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setStyleSheet("\n"
"background-color: #bc8f8f;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 1, 4)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget.setStyleSheet("alternate-background-color: #0047AB;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setStyleSheet("color: #000000;\n"
"background-color: #ffe5b4;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"border: none;\n"
"box-shadow: 0 0 10px 5px rgba(221, 221, 221, 1);\n"
"width: 30px;\n"
"height: 30px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_3.setStyleSheet("background-color: #f2f2f2;\n"
"")
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_2.addWidget(self.listWidget_3, 1, 1, 2, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.crbt_notes.setText(_translate("MainWindow", "+"))
        self.refresh.setText(_translate("MainWindow", "обновить"))
        self.deletebt_notes.setText(_translate("MainWindow", "удалить"))
        self.editi.setText(_translate("MainWindow", "редактирование"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Заметки"))
        self.crbt_tasks.setText(_translate("MainWindow", "+"))
        self.refresh_2.setText(_translate("MainWindow", "обновить"))
        self.deletebt_notes_2.setText(_translate("MainWindow", "удалить"))
        self.editi_2.setText(_translate("MainWindow", "редактирование"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Задачи"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "удалить"))
        self.pushButton_2.setText(_translate("MainWindow", "♲"))
        self.label.setText(_translate("MainWindow", "Ввод"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Календарь"))