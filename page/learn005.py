#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn005.py
# @Author: Luopan
# @Date  : 2018/8/6 16:30
# @Desc  : 弹窗确认是否关闭窗口
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon

icon_name = u"刷新"
icon_path = r"D://project_pro//PyQt5-learn//icons//refresh.png"

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(icon_name)
        self.setWindowIcon(QIcon(icon_path))
        self.show()

    '''重写QCloseEvent的closeEvent'''
    def closeEvent(self, event):
        '''带两个按钮的message box：YES和No按钮。
        代码中第一个字符串的内容被显示在标题栏上。
        第二个字符串是对话框上显示的文本。
        第三个参数指定了显示在对话框上的按钮集合。
        最后一个参数是默认选中的按钮。这个按钮一开始就获得焦点。
        返回值被储存在reply变量中'''
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())