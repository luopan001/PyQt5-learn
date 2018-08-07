#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn003.py
# @Author: Luopan
# @Date  : 2018/8/6 16:00
# @Desc  : 显示一个提示文本
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont,QIcon

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

        '''创建一个按钮'''
        btn = QPushButton('Button', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')
        '''给按钮设置推荐的尺寸'''
        btn.resize(btn.sizeHint())
        '''移动按钮到一个位置，这个位置是窗口上x=300,y=300的坐标'''
        btn.move(50, 50)

        '''（1）创建气泡提示框（2）提示框的大小，字体为默认'''
        #QToolTip.setFont(QFont())
        '''（1）创建气泡提示框（2）提示框使用10px大小的SansSerif字体'''
        QToolTip.setFont(QFont('SansSerif', 30))
        '''为按钮添加气泡提示'''
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        '''在屏幕上显示出widge'''
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())