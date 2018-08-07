#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn008.py
# @Author: Luopan
# @Date  : 2018/8/6 17:20
# @Desc  : 菜单栏
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
        '''创建有一个菜单项的菜单栏。这个菜单项包含一个选中后中断应用的动作'''
        exitAction = QAction(QIcon(icon_path), '&Exit', self)
        '''定义快捷键'''
        exitAction.setShortcut('Ctrl+Q')
        '''创建一个当我们鼠标浮于菜单项之上就会显示的一个状态提示。'''
        exitAction.setStatusTip('Exit application')
        '''当我们选中特定的动作，一个触发信号会被发射。信号连接到QApplication组件的quit()方法。这样就中断了应用'''
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        '''menuBar()方法创建了一个菜单栏'''
        fileMenu = menubar.addMenu('&File')
        '''创建一个file菜单，然后将退出动作添加到file菜单中'''
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())