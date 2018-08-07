#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn006.py
# @Author: Luopan
# @Date  : 2018/8/6 16:50
# @Desc  : 窗口居中
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon

icon_name = u"刷新"
icon_path = r"D://project_pro//PyQt5-learn//icons//refresh.png"


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''窗口的宽，高分别设置为250px,150px'''
        self.resize(250, 150)
        '''调用窗口居中函数'''
        self.center()
        self.setWindowTitle(icon_name)
        self.setWindowIcon(QIcon(icon_path))
        self.show()

    def center(self):
        '''获得主窗口的一个矩形特定几何图形'''
        qr = self.frameGeometry()
        '''算出相对于显示器的绝对值。并且从这个绝对值中，我们获得了屏幕中心点'''
        cp = QDesktopWidget().availableGeometry().center()
        '''把矩形的中心设置到屏幕的中间去。矩形的大小并不会改变'''
        qr.moveCenter(cp)
        '''移动了应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上'''
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())