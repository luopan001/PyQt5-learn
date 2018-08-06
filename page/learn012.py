#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn007.py
# @Author: Luopan
# @Date  : 2018/8/6 17:20
# @Desc  : 箱布局：在右下角放置了两个按钮。当我们改变应用窗口大小时，它们会相对于应用窗口不改变位置
# @other : PyQt5-5.11.2 Python-3.6

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        '''创建了一个水平箱布局，并且增加了一个拉伸因子和两个按钮。拉伸因子在两个按钮之前增加了一个可伸缩空间。这会将按钮推到窗口的右边。'''
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        '''水平布局放置在垂直布局内。拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边'''
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())