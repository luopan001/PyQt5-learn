#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test001.py
# @Author: Luopan
# @Date  : 2018/8/7 16:30
# @Desc  : 信号与槽的绑定
# @other : PyQt5-5.11.2 Python-3.6、PyQt5Designer-5.10.1(设计时选择MainWindow)、PyUIC

from PyQt5 import QtCore, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 190, 150, 23))
        self.pushButton.setObjectName("pushbutton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(340, 250, 150, 23))
        self.pushButton1.setObjectName("pushbutton")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        MainWindow.show()

        # 同一个信号绑定多个槽
        self.pushButton.clicked.connect(self.firtPyQt5_button_click1)
        self.pushButton.clicked.connect(self.firtPyQt5_button_click2)

        # 一个信号绑定另一个信号
        self.pushButton1.clicked.connect(self.pushButton.clicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "同一个信号绑定多个槽"))
        self.pushButton1.setText(_translate("MainWindow", "一个信号绑定另一个信号"))

    def firtPyQt5_button_click1(self):
        QtWidgets.QMessageBox.information(self.pushButton, "标题1", "槽函数1")

    def firtPyQt5_button_click2(self):
        QtWidgets.QMessageBox.information(self.pushButton, "标题2", "槽函数2")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    #widget.show()
    sys.exit(app.exec_())