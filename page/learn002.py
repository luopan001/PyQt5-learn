#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn002.py
# @Author: Luopan
# @Date  : 2018/8/6 16:00
# @Desc  : 应用图标的创建
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

icon_name = u"刷新"
icon_path = r"D://project_pro//PyQt5-learn//icons//refresh.png"

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''（1）创建窗口。（2）设置宽300px,高300px。（3）移动widget组件到一个位置，这个位置是屏幕上x=300,y=300的坐标。'''
        self.setGeometry(300, 300, 300, 220)
        '''设置窗体名称'''
        self.setWindowTitle(icon_name)
        '''设置窗体图标'''
        self.setWindowIcon(QIcon(icon_path))
        '''在屏幕上显示出widge'''
        self.show()


if __name__ == '__main__':
    '''参见learn001.py的说明'''
    app = QApplication(sys.argv)
    ex = Example()
    '''参见learn001.py的说明'''
    sys.exit(app.exec_())