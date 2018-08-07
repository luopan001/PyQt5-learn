#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn018.py
# @Author: Luopan
# @Date  : 2018/8/7 10:00
# @Desc  : 发送信号。当我们在窗口上点击一下鼠标，closeApp信号会被发射。应用中断。
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())