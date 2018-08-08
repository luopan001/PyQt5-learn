#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test001.py
# @Author: Luopan
# @Date  : 2018/8/7 17:30
# @Desc  : 自定义信号，非QtDesigner生成
'''
新的信号应该定义在QObject的子类中。新的信号必须作为定义类的一部分，不允许将信号作为类的属性在类定义之后通过动态的方式进行添加。
通过这种方式新的信号才能自动的添加到QMetaObject类中。这就意味这新定义的信号将会出现在Qt Designer，
并且可以通过QMetaObject API实现内省
'''

import sys
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QCheckBox, QSpinBox, QHBoxLayout, \
    QComboBox, QGridLayout


class SignalEmit(QWidget):
    # 定义信号 helpSignal
    helpSignal = pyqtSignal(str)
    # 定义信号 printSignal
    printSignal = pyqtSignal(list)
    # 定义信号 previewSignal，一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([int, str], [str])

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.creatContorls("打印控制：")
        self.creatResult("操作结果：")

        # 创建水平箱布局，将打印控制区域与操作结果区域水平布局
        layout = QHBoxLayout()
        # 向水平箱布局加入打印控制区域
        layout.addWidget(self.controlsGroup)
        # 向水平线布局加入操作结果区域
        layout.addWidget(self.resultGroup)
        self.setLayout(layout)

        # 将信号 helpSignal 与槽函数 showHelpMessage 绑定

        self.helpSignal.connect(self.showHelpMessage)
        # 将信号 printSignal 与槽函数 printPaper 绑定
        self.printSignal.connect(self.printPaper)
        # 将信号 previewSignal[str] 与槽函数 previewPaper 绑定
        self.previewSignal[str].connect(self.previewPaper)
        # 将信号 previewSignal[int, str] 与槽函数 previewPaperWithArgs 绑定
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)
        # 将打印按钮的信号 clicked 与槽函数 emitPrintSignal 绑定
        self.printButton.clicked.connect(self.emitPrintSignal)
        # 将打印按钮的信号 clicked 与槽函数 emitPreviewSignal 绑定
        self.previewButton.clicked.connect(self.emitPreviewSignal)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('自定义信号')
        self.show()

    # 定义打印控制区域的相关元素及布局
    def creatContorls(self, title):
        # 创建一个带标题的组合框 controlsGroup（组合框提供一个框架、一个标题和一个键盘快捷键，并且显示在它里面地其它不同窗口部件）
        self.controlsGroup = QGroupBox(title)
        # 创建打印按钮 printButton
        self.printButton = QPushButton("打印")
        # 创建预览按钮 previewButton
        self.previewButton = QPushButton("预览")
        # 创建打印份数标签 numberLabel
        numberLabel = QLabel("打印份数：")
        # 创建纸张类型标签 pageLabel
        pageLabel = QLabel("纸张类型：")
        # 创建全屏预览复选框 previewStatus
        self.previewStatus = QCheckBox("全屏预览")
        # 创建打印份数微调框 numberSpinBox
        self.numberSpinBox = QSpinBox()
        # 设置打印份数微调框的值在1~100之间
        self.numberSpinBox.setRange(1, 100)

        # 创建纸张类型下拉列表框 styleCombo
        self.styleCombo = QComboBox(self)
        # 为 styleCombo 增加选项“A4”
        self.styleCombo.addItem("A4")
        # 为 styleCombo 增加选项“A5”
        self.styleCombo.addItem("A5")

        # 创建网格布局
        controlsLayout = QGridLayout()
        # 向网格布局中增加打印份数标签 numberLabel，位置在0,0
        controlsLayout.addWidget(numberLabel, 0, 0)
        # 向网格布局中增加打印份数微调框 numberSpinBox，位置在0,1
        controlsLayout.addWidget(self.numberSpinBox, 0, 1)
        # 向网格布局中增加纸张类型标签 pageLabel，位置在0,2
        controlsLayout.addWidget(pageLabel, 0, 2)
        # 向网格布局中增加纸张类型下拉列表框 styleCombo，位置在0,3
        controlsLayout.addWidget(self.styleCombo, 0, 3)
        # 向网格布局中增加打印按钮 printButton，位置在0,4
        controlsLayout.addWidget(self.printButton, 0, 4)
        # 向网格布局中增加全屏预览复选框 previewStatus，位置在3,0
        controlsLayout.addWidget(self.previewStatus, 3, 0)
        # 向网格布局中增加预览按钮 previewButton，位置在3,1
        controlsLayout.addWidget(self.previewButton, 3, 1)
        # 对组合框进行网格布局
        self.controlsGroup.setLayout(controlsLayout)

    # 定义操作结果区域的相关元素及布局
    def creatResult(self, title):
        self.resultGroup = QGroupBox(title)
        self.resultLabel = QLabel("")
        layout = QHBoxLayout()
        layout.addWidget(self.resultLabel)
        self.resultGroup.setLayout(layout)

    # 定义槽函数 emitPreviewSignal
    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int, str].emit(1080, " Full Screen")
        elif self.previewStatus.isChecked() == False:
            self.previewSignal[str].emit("Preview")

    # 定义槽函数 emitPrintSignal
    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    # 定义槽函数 printPaper
    def printPaper(self, list):
        self.resultLabel.setText("Print: " + "份数：" + str(list[0]) + " 纸张：" + str(list[1]))

    # 定义槽函数 previewPaperWithArgs
    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)

    # 定义槽函数 previewPaper
    def previewPaper(self, text):
        self.resultLabel.setText(text)

    # 定义事件 keyPressEvent
    def keyPressEvent(self, event):

        if event.key() == Qt.Key_F1:
            # 发射信号 helpSignal
            self.helpSignal.emit("help message")

    # 定义槽函数 showHelpMessage
    def showHelpMessage(self, message):
        self.resultLabel.setText(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dispatch = SignalEmit()
    sys.exit(app.exec_())