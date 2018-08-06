#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn001.py
# @Author: Luopan
# @Date  : 2018/8/6 15:00
# @Desc  : 窗体创建
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    '''所有的PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。'''
    app = QApplication(sys.argv)
    '''创建窗口'''
    w = QWidget()
    '''调整widget组件的大小。宽250px，高150px'''
    w.resize(250, 150)
    '''移动widget组件到一个位置，这个位置是屏幕上x=300,y=300的坐标'''
    w.move(300, 300)
    '''设置了我们窗口的标题。这个标题显示在标题栏中'''
    w.setWindowTitle('Simple')
    '''在屏幕上显示出widge'''
    w.show()
    '''进入程序的主循环接收来自窗口触发的事件，并且转发到widget应用上处理'''
    app.exec_()
    '''退出应用'''
    sys.exit()