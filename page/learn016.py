#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn016.py
# @Author: Luopan
# @Date  : 2018/8/7 09:40
# @Desc  : 重写事件处理函数，点击Esc，应用会终止
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())