#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn004.py
# @Author: Luopan
# @Date  : 2018/8/6 16:30
# @Desc  : 关闭窗口
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


icon_name = u"刷新"
icon_path = r"D://project_pro//PyQt5-learn//icons//refresh.png"

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''（1）创建窗口（2）设置窗口大小及位置（3）设置窗口应用图标'''
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle(icon_name)
        self.setWindowIcon(QIcon(icon_path))
        '''创建一个Quit按钮'''
        qbtn = QPushButton('Quit', self)
        '''事件处理系统由信号&槽机制建立。如果我们点击了按钮，信号clicked被发送。
        槽可以是Qt内置的槽或Python 的一个方法调用。QCoreApplication类包含了主事件循环；
        它处理和转发所有事件。instance()方法给我们返回一个实例化对象。注意QCoreAppli类
        由QApplication创建。点击信号连接到quit()方法，将结束应用。事件通信在两个对象之
        间进行：发送者和接受者。发送者是按钮，接受者是应用对象。'''
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        '''设置按钮为推荐的大小'''
        qbtn.resize(qbtn.sizeHint())
        '''移动按钮到一个位置，这个位置是窗口上x=300,y=300的坐标'''
        qbtn.move(50, 50)
        '''在屏幕上显示出widge'''
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())