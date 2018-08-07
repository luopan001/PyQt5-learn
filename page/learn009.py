#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn009.py
# @Author: Luopan
# @Date  : 2018/8/6 17:20
# @Desc  : 工具栏
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

icon_path = r"D://project_pro//PyQt5-learn//icons//logout.png"

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        '''定义exitAction动作'''
        exitAction = QAction(QIcon(icon_path), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())