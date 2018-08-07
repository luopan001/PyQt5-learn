#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn007.py
# @Author: Luopan
# @Date  : 2018/8/6 17:20
# @Desc  : 状态栏
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''调用了QtGui.QMainWindow类的statusBar()方法,创建状态栏'''
        statuscoulunm = self.statusBar()
        '''显示信息Ready'''
        statuscoulunm.showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())