#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : .py
# @Author: Luopan
# @Date  : 2018/8/8 14:30
# @Desc  : android，monkey测试辅助小工具。 本版本适用于pyinstaller打包生成exe文件运行。v2.0(正式版)

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os,re,subprocess,logging,time
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5 import sip

project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
icon_path = "D:\\project_pro\\PyQt5-learn\\test\\android.png"

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.mainUI(self)
        self.retranslateUi(self)
        self.aapt_path = self.get_aapt()
        self.logger = Log()


    def mainUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 915)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(51, 20, 621, 756))
        self.widget.setObjectName("widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.printDeviceInfo = QtWidgets.QPlainTextEdit(self.groupBox)
        self.printDeviceInfo.setObjectName("printDeviceInfo")
        self.verticalLayout_3.addWidget(self.printDeviceInfo)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.deviceInfo = QtWidgets.QPushButton(self.groupBox)
        self.deviceInfo.setObjectName("deviceInfo")
        self.horizontalLayout_8.addWidget(self.deviceInfo)
        self.deviceRst = QtWidgets.QPushButton(self.groupBox)
        self.deviceRst.setObjectName("deviceRst")
        self.horizontalLayout_8.addWidget(self.deviceRst)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.printAppRoute = QtWidgets.QLineEdit(self.groupBox_2)
        self.printAppRoute.setObjectName("printAppRoute")
        self.horizontalLayout.addWidget(self.printAppRoute)
        self.getAppRoute = QtWidgets.QPushButton(self.groupBox_2)
        self.getAppRoute.setObjectName("getAppRoute")
        self.horizontalLayout.addWidget(self.getAppRoute)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.appName_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.appName_1.setObjectName("appName")
        self.verticalLayout.addWidget(self.appName_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.installBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.installBtn.setObjectName("installBtn")
        self.horizontalLayout_2.addWidget(self.installBtn)
        self.installBtn_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.installBtn_2.setObjectName("installBtn_2")
        self.horizontalLayout_2.addWidget(self.installBtn_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uninstallBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.uninstallBtn.setObjectName("uninstallBtn")
        self.horizontalLayout_3.addWidget(self.uninstallBtn)
        self.installBtn_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.installBtn_3.setObjectName("installBtn_3")
        self.horizontalLayout_3.addWidget(self.installBtn_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.printAppRoute_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.printAppRoute_2.setObjectName("printAppRoute_2")
        self.horizontalLayout_4.addWidget(self.printAppRoute_2)
        self.geiAppRoute_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.geiAppRoute_2.setObjectName("geiAppRoute_2")
        self.horizontalLayout_4.addWidget(self.geiAppRoute_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.printAppInfo = QtWidgets.QTextEdit(self.groupBox_3)
        self.printAppInfo.setObjectName("printAppInfo")
        self.verticalLayout_2.addWidget(self.printAppInfo)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.getAppInfo = QtWidgets.QPushButton(self.groupBox_3)
        self.getAppInfo.setObjectName("getAppInfo")
        self.horizontalLayout_5.addWidget(self.getAppInfo)
        self.appReset = QtWidgets.QPushButton(self.groupBox_3)
        self.appReset.setObjectName("appReset")
        self.horizontalLayout_5.addWidget(self.appReset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.appname = QtWidgets.QLabel(self.groupBox_4)
        self.appname.setObjectName("appname")
        self.verticalLayout_7.addWidget(self.appname)
        self.throlttle = QtWidgets.QLabel(self.groupBox_4)
        self.throlttle.setObjectName("throlttle")
        self.verticalLayout_7.addWidget(self.throlttle)
        self.infograde = QtWidgets.QLabel(self.groupBox_4)
        self.infograde.setObjectName("infograde")
        self.verticalLayout_7.addWidget(self.infograde)
        self.count = QtWidgets.QLabel(self.groupBox_4)
        self.count.setObjectName("count")
        self.verticalLayout_7.addWidget(self.count)
        self.seed = QtWidgets.QLabel(self.groupBox_4)
        self.seed.setObjectName("seed")
        self.verticalLayout_7.addWidget(self.seed)
        self.touch = QtWidgets.QLabel(self.groupBox_4)
        self.touch.setObjectName("touch")
        self.verticalLayout_7.addWidget(self.touch)
        self.motion = QtWidgets.QLabel(self.groupBox_4)
        self.motion.setObjectName("motion")
        self.verticalLayout_7.addWidget(self.motion)

        self.pinch = QtWidgets.QLabel(self.groupBox_4)
        self.pinch.setObjectName("pinch")
        self.verticalLayout_7.addWidget(self.pinch)
        self.screen = QtWidgets.QLabel(self.groupBox_4)
        self.screen.setObjectName("screen")
        self.verticalLayout_7.addWidget(self.screen)
        self.keyboard = QtWidgets.QLabel(self.groupBox_4)
        self.keyboard.setObjectName("keyboard")
        self.verticalLayout_7.addWidget(self.keyboard)

        self.trackball = QtWidgets.QLabel(self.groupBox_4)
        self.trackball.setObjectName("trackball")
        self.verticalLayout_7.addWidget(self.trackball)
        self.nav = QtWidgets.QLabel(self.groupBox_4)
        self.nav.setObjectName("nav")
        self.verticalLayout_7.addWidget(self.nav)
        self.majornav = QtWidgets.QLabel(self.groupBox_4)
        self.majornav.setObjectName("majornav")
        self.verticalLayout_7.addWidget(self.majornav)
        self.syskeys = QtWidgets.QLabel(self.groupBox_4)
        self.syskeys.setObjectName("syskeys")
        self.verticalLayout_7.addWidget(self.syskeys)
        self.appswitch = QtWidgets.QLabel(self.groupBox_4)
        self.appswitch.setObjectName("appswitch")
        self.verticalLayout_7.addWidget(self.appswitch)
        self.anyevent = QtWidgets.QLabel(self.groupBox_4)
        self.anyevent.setObjectName("anyevent")
        self.verticalLayout_7.addWidget(self.anyevent)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.appnameInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.appnameInput.setObjectName("appnameInput")
        self.verticalLayout_6.addWidget(self.appnameInput)
        self.throttleInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.throttleInput.setObjectName("throttleInput")
        self.verticalLayout_6.addWidget(self.throttleInput)
        self.infogradeChoose = QtWidgets.QComboBox(self.groupBox_4)
        self.infogradeChoose.setObjectName("comboBox")
        self.infogradeChoose.addItem("")
        self.infogradeChoose.addItem("")
        self.infogradeChoose.addItem("")
        self.verticalLayout_6.addWidget(self.infogradeChoose)
        self.countInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.countInput.setObjectName("countInput")
        self.verticalLayout_6.addWidget(self.countInput)
        self.seedInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.seedInput.setObjectName("seedInput")
        self.verticalLayout_6.addWidget(self.seedInput)
        self.touchInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.touchInput.setObjectName("touchInput")
        self.verticalLayout_6.addWidget(self.touchInput)
        self.motionInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.motionInput.setObjectName("motionInput")
        self.verticalLayout_6.addWidget(self.motionInput)

        self.pinchInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.pinchInput.setObjectName("pinchInput")
        self.verticalLayout_6.addWidget(self.pinchInput)
        self.screenInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.screenInput.setObjectName("screenInput")
        self.verticalLayout_6.addWidget(self.screenInput)
        self.keyboardInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.keyboardInput.setObjectName("keyboardInput")
        self.verticalLayout_6.addWidget(self.keyboardInput)

        self.trackballInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.trackballInput.setObjectName("trackballInput")
        self.verticalLayout_6.addWidget(self.trackballInput)
        self.navInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.navInput.setObjectName("navInput")
        self.verticalLayout_6.addWidget(self.navInput)
        self.majornavInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.majornavInput.setObjectName("majornavInput")
        self.verticalLayout_6.addWidget(self.majornavInput)
        self.sysykeysInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.sysykeysInput.setObjectName("sysykeysInput")
        self.verticalLayout_6.addWidget(self.sysykeysInput)
        self.appswitchInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.appswitchInput.setObjectName("appswitchInput")
        self.verticalLayout_6.addWidget(self.appswitchInput)
        self.anyeventInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.anyeventInput.setObjectName("anyeventInput")
        self.verticalLayout_6.addWidget(self.anyeventInput)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.monkeyTestBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.monkeyTestBtn.setObjectName("monkeyTestBtn")
        self.horizontalLayout_6.addWidget(self.monkeyTestBtn)
        self.viewlogBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.viewlogBtn.setObjectName("viewlogBtn")
        self.horizontalLayout_6.addWidget(self.viewlogBtn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.remark = QtWidgets.QLabel(self.groupBox_5)
        self.remark.setObjectName("remark")
        self.verticalLayout_9.addWidget(self.remark)
        self.verticalLayout_10.addWidget(self.groupBox_5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        self.deviceInfo.clicked.connect(self.get_device_info)
        self.deviceRst.clicked.connect(self.printDeviceInfo.clear)
        #self.deviceRst_2.clicked.connect(self.view_getdevices_log)
        self.installBtn.clicked.connect(self.install_app)
        self.installBtn_2.clicked.connect(self.view_log)
        self.uninstallBtn.clicked.connect(self.uninstall_app)
        self.installBtn_3.clicked.connect(self.view_log)
        self.getAppInfo.clicked.connect(self.get_app_info)
        self.groupBox_3.clicked.connect(self.printAppInfo.clear)
        self.monkeyTestBtn.clicked.connect(self.monkey_test)
        self.viewlogBtn.clicked.connect(self.view_log)
        self.getAppRoute.clicked.connect(self.get_windows_file_1)
        self.geiAppRoute_2.clicked.connect(self.get_windows_file_2)
        self.appReset.clicked.connect(self.printAppInfo.clear)
        self.groupBox.clicked.connect(self.printDeviceInfo.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "安卓自动化测试-monkey"))
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))
        self.groupBox.setTitle(_translate("MainWindow", "设备信息"))
        self.deviceInfo.setText(_translate("MainWindow", "获取设备信息"))
        self.deviceRst.setText(_translate("MainWindow", "重置"))
        self.groupBox_2.setTitle(_translate("MainWindow", "安装卸载测试"))
        self.label.setText(_translate("MainWindow", "安装包路径"))
        self.getAppRoute.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "卸载包名"))
        self.installBtn.setText(_translate("MainWindow", "点击安装"))
        self.installBtn_2.setText(_translate("MainWindow", "查看安装日志"))
        self.uninstallBtn.setText(_translate("MainWindow", "点击卸载"))
        self.installBtn_3.setText(_translate("MainWindow", "查看卸载日志"))
        self.groupBox_3.setTitle(_translate("MainWindow", "应用信息"))
        self.label_3.setText(_translate("MainWindow", "安装包路径"))
        self.geiAppRoute_2.setText(_translate("MainWindow", "浏览"))
        self.getAppInfo.setText(_translate("MainWindow", "获取应用信息"))
        self.appReset.setText(_translate("MainWindow", "重置"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Monkey"))
        self.appname.setText(_translate("MainWindow", "包名（-p)"))
        self.throlttle.setText(_translate("MainWindow", "行为延时(-throttle)"))
        self.infograde.setText(_translate("MainWindow", "输出结果详细级别(-v)"))
        self.count.setText(_translate("MainWindow", "随机事件数(count)"))
        self.seed.setText(_translate("MainWindow", "重现种子数(s)"))
        self.touch.setText(_translate("MainWindow", "触摸事件%（touch）"))
        self.motion.setText(_translate("MainWindow", "动作事件%（motion）"))
        self.screen.setText(_translate("MainWindow", "屏幕旋转%（screen）"))
        self.pinch.setText(_translate("MainWindow", "二指缩放事件%（pinch）"))
        self.keyboard.setText(_translate("MainWindow", "键盘事件%（keyboard）"))
        self.trackball.setText(_translate("MainWindow", "轨迹球事件%（trackball）"))
        self.nav.setText(_translate("MainWindow", "基本导航事件%（nav）"))
        self.majornav.setText(_translate("MainWindow", "主要导航事件%（majornav）"))
        self.syskeys.setText(_translate("MainWindow", "系统关键事件%（syskeys）"))
        self.appswitch.setText(_translate("MainWindow", "启动活动事件%(appswitch)"))
        self.anyevent.setText(_translate("MainWindow", "其他类型事件%（anyevent）"))
        self.infogradeChoose.setItemText(0, _translate("MainWindow", "简单"))
        self.infogradeChoose.setItemText(1, _translate("MainWindow", "一般"))
        self.infogradeChoose.setItemText(2, _translate("MainWindow", "详细"))
        self.monkeyTestBtn.setText(_translate("MainWindow", "执行monkey测试"))
        self.viewlogBtn.setText(_translate("MainWindow", "查看日志"))
        self.groupBox_5.setTitle(_translate("MainWindow", "备注信息"))
        remark_string = "1、环境检查\n1)请首先配置安卓环境（aapt环境）\n2)请安装安卓手机模拟器或者插入真机进行测试，配置好adb\n" \
                        "2、获取应用信息的匹配规则请根据所测app灵活进行调整\n3、开发人员信息\n1) 姓名：luopan\n2）联系方式：XXXXX"
        self.remark.setText(remark_string)
        self.appName_1.clear()
        self.input_clear()

        # 0~100以内的数值，最多保留2位小数，包含各自的边界值。
        regx = QRegExp("^(\d?\d(\.\d{1,2})?|100)$")
        validator = QRegExpValidator(regx, self.throttleInput)
        self.throttleInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.touchInput)
        self.touchInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.motionInput)
        self.motionInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.trackballInput)
        self.trackballInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.navInput)
        self.navInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.majornavInput)
        self.majornavInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.sysykeysInput)
        self.sysykeysInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.anyeventInput)
        self.anyeventInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.appswitchInput)
        self.appswitchInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.pinchInput)
        self.pinchInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.screenInput)
        self.screenInput.setValidator(validator)
        validator = QRegExpValidator(regx, self.keyboardInput)
        self.keyboardInput.setValidator(validator)
        # 正整数的表达式，不包括0
        regx1 = QRegExp("^[1-9]\d*$")
        validator = QRegExpValidator(regx1, self.countInput)
        self.countInput.setValidator(validator)
        # 正整数的表达式，包括0
        regx2 = QRegExp("^[+]{0,1}(\d+)$")
        validator = QRegExpValidator(regx2, self.throttleInput)
        self.throttleInput.setValidator(validator)

    # 获取设备信息
    def get_device_info(self):
        try:
            cmd = 'adb devices'
            self.info = os.popen(cmd).readlines()
            self.deviceid = self.info[1].split('\t')[0]
            # 获取手机系统版本
            self.version = os.popen('adb shell getprop ro.build.version.release').readlines()[0].split('\r\n')[0]
            self.printDeviceInfo.setPlainText("设备ID："+self.deviceid+"\n"+"手机版本："+self.version)
        except:
            QMessageBox.information(self,"信息确认","请检查：\n1）设备是否已连接模拟器或者真机\n2）adb命令是否设置正确",QMessageBox.NoButton)



    # 安装卸载测试：获取安装包路径
    def get_windows_file_1(self):
        try:
            self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, '选择应用安装包', '/', 'Apk Files (*.apk)')
            self.printAppRoute.setText(self.filename)
        except:
            pass

    # 应用信息：获取安装包路径，点击应用信息模块的“浏览”按钮
    def get_windows_file_2(self):
        try:
            self.filename_1, _ =  QtWidgets.QFileDialog.getOpenFileName(self, '选择应用安装包', '/', 'Apk Files (*.apk)')
            self.printAppRoute_2.setText(self.filename_1)
        except:
            pass

    # 获取应用信息：点击“获取应用信息”按钮
    def get_app_info(self):
        try:
            Size = self.get_app_size()
            t = self.get_app_base_info()
            app_info_string = "包名：" + t[0] + "\n" + "版本号：" + t[1] +"\n" + "版本名称：" + t[2] + "\n" + "包的大小：" + str(Size) + " M" + "\n"+ "启动类：" + t[3]+"\n"
            self.printAppInfo.setText(app_info_string)
        except:
            QMessageBox.warning(self, "警告", "请先上传安装包", QMessageBox.NoButton)

    #  获取安装包的大小
    def get_app_size(self):
        try:
            if self.printAppRoute_2.text() is not None:
                size = round(os.path.getsize(self.printAppRoute_2.text()) / (1024 * 1000), 2)
                self.logger.info("size")
                return size
        except:
            pass

    # 获取安装包的基本信息：包名，版本号，版本名称
    def get_app_base_info(self):
        try:
            if self.printAppRoute_2.text() is not None:
                cmd = self.aapt_path + ' dump badging ' + self.printAppRoute_2.text()
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
                match_1 = re.compile("launchable-activity: name='(\S+)'  label=").search(output.decode())
                package_name = match.group(1)
                version_code = match.group(2)
                version_name = match.group(3)
                launchable_activity_name = match_1.group(1)
                return (package_name,version_code,version_name,launchable_activity_name)
        except:
            pass

    # 安装app
    def install_app(self):
        try:
            if self.printAppRoute.text().strip():
                cmd = "adb install " + self.printAppRoute.text()
                f = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
                QMessageBox.information(self, "提示", "请5秒后查看安装结果", QMessageBox.NoButton)
                while f.poll() is None:
                    line = f.stdout.readline()
                    line = line.strip()
                    if line:
                        self.logger.info(line)
                if f.returncode==0:
                    self.logger.info("subprocess Success")
                else:
                    self.logger.error("subprocess Failed")
                f.kill()
            else:
                QMessageBox.warning(self, "警告", "请先上传安装包", QMessageBox.NoButton)
        except:
            pass

    def view_log(self):
        QMessageBox.information(self, "日志查看", "请到Log目录查看", QMessageBox.NoButton)

    # 卸载app
    def uninstall_app(self):
        try:
            if self.appName_1.text().strip():
                cmd = "adb uninstall " + self.appName_1.text()
                data = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
                QMessageBox.information(self, "提示", "请5秒后查看安装结果", QMessageBox.NoButton)
                while data.poll() is None:
                    line = data.stdout.readline()
                    line = line.strip()
                    if line:
                        self.logger.info(line)
                if data.returncode==0:
                    self.logger.info("subprocess Success")
                else:
                    self.logger.error("subprocess Failed")
                data.kill()
            else:
                QMessageBox.warning(self, "警告", "请输入包名（可通过应用信息模块-获取应用信息得到包名）", QMessageBox.NoButton)
        except:
            pass


    # monkey测试
    def monkey_test(self):
        cmd = "adb shell monkey"
        # 测试的包名
        try:
            if self.appnameInput.text().strip():
                cmd = cmd +  " -p " + self.appnameInput.text()
                cmd = self.monkey_test_1(cmd)
                if self.countInput.text().strip():
                    cmd = cmd + " " +self.countInput.text()
                    self.logger.info("monkey command is :")
                    self.logger.info(cmd)
                    if self.judge_sum() is True:
                        self.run_command(cmd)
                    else:
                        QMessageBox.warning(self, "警告", "所有事件之和必须等于100", QMessageBox.NoButton)
                else:
                    QMessageBox.warning(self, "警告", "请输入随机事件数(count)", QMessageBox.NoButton)
            else:
                QMessageBox.warning(self, "警告", "请输入包名（可通过应用信息模块-获取应用信息得到包名）", QMessageBox.NoButton)
        except:
            pass

    def judge_sum(self):
        try:
            # 若11个事件的输入项都为空，则由系统随机分配执行比例
            if (not self.touchInput.text().strip()) and (not self.motionInput.text().strip()) and \
                    (not self.pinchInput.text().strip()) and (not self.keyboardInput.text().strip()) and \
                    (not self.navInput.text().strip()) and (not self.majornavInput.text().strip()) and \
                    (not self.sysykeysInput.text().strip()) and (not self.anyeventInput.text().strip()) and \
                    (not self.appswitchInput.text().strip()) and (not self.screenInput.text().strip()) and \
                    (not self.trackballInput.text().strip()):
                return True
            else:
                # 若11个事件的输入项有一个不为空，则必须满足所有事件之和等于100%
                if self.touchInput.text().strip():
                    sum_1 = float(self.touchInput.text())
                if self.motionInput.text().strip():
                    sum_1 = sum_1 + float(self.motionInput.text())
                if self.pinchInput.text().strip():
                    sum_1 = sum_1 + float(self.pinchInput.text())
                if self.screenInput.text().strip():
                    sum_1 = sum_1 + float(self.screenInput.text())
                if self.navInput.text().strip():
                    sum_1 = sum_1 + float(self.navInput.text())
                if self.majornavInput.text().strip():
                    sum_1 = sum_1 + float(self.majornavInput.text())
                if self.trackballInput.text().strip():
                    sum_1 = sum_1 + float(self.trackballInput.text())
                if self.sysykeysInput.text().strip():
                    sum_1 = sum_1 + float(self.sysykeysInput.text())
                if self.anyeventInput.text().strip():
                    sum_1 = sum_1 + float(self.anyeventInput.text())
                if self.keyboardInput.text().strip():
                    sum_1 = sum_1 + float(self.keyboardInput.text())
                if self.appswitchInput.text().strip():
                    sum_1 = sum_1 + float(self.appswitchInput.text())
                print("234")
                print(sum_1)
                if sum_1 == 100.00:
                    return True
        except:
            pass

    def input_clear(self):
        self.touchInput.clear()
        self.motionInput.clear()
        self.pinchInput.clear()
        self.trackballInput.clear()
        self.screenInput.clear()
        self.appswitchInput.clear()
        self.anyeventInput.clear()
        self.sysykeysInput.clear()
        self.majornavInput.clear()
        self.navInput.clear()
        self.keyboardInput.clear()

    def monkey_test_1(self,cmd):
        # 用于指定用户操作（即事件）间的时延，单位是毫秒
        try:
            if self.throttleInput.text().strip():
                cmd = cmd +  " --throttle " + self.throttleInput.text()
        except:
            pass

        # 日志信息
        try:
            if self.infogradeChoose.currentText()==u'简单':
                # 说明缺省值，仅提供启动提示、测试完成和最终结果等少量信息
                cmd = cmd + " -v"
            elif self.infogradeChoose.currentText()==u'一般':
                # 说明提供较为详细的日志，包括每个发送到Activity的事件信息
                cmd = cmd + " -v -v"
            else:
                # 说明最详细的日志，包括了测试中选中/未选中的Activity信息
                cmd = cmd + " -v -v -v"
        except:
            pass

        # 用于指定伪随机数生成器的seed值，如果seed相同，则两次Monkey测试所产生的事件序列也相同的
        try:
            if self.seedInput.text().strip():
                cmd = cmd +  "  -s " + self.seedInput.text()
            # 调整触摸事件的百分比(触摸事件是一个down-up事件，它发生在屏幕上的某单一位置)
            if self.touchInput.text().strip():
                cmd = cmd + "  --pct-touch " + self.touchInput.text()
            # 调整动作事件的百分比(动作事件由屏幕上某处的一个down事件、一系列的伪随件机事和一个up事件组成)
            if self.motionInput.text().strip():
                cmd = cmd + "  --pct-motion " + self.motionInput.text()
            # 调整轨迹事件的百分比(轨迹事件由一个或几个随机的移动组成，有时还伴随有点击)
            if self.trackballInput.text().strip():
                cmd = cmd + "  --pct-trackball " + self.trackballInput.text()
            # 调整“基本”导航事件的百分比(导航事件由来自方向输入设备的up/down/left/right组成)
            if self.navInput.text().strip():
                cmd = cmd + "  --pct-nav " + self.navInput.text()
            #  调整“主要”导航事件的百分比(这些导航事件通常引发图形界面中的动作，如：5-way键盘的中间按键、回退按键、菜单按键)
            if self.majornavInput.text().strip():
                cmd = cmd + "  --pct-majornav " + self.majornavInput.text()
            if self.sysykeysInput.text().strip():
                cmd = cmd + "  --pct-syskeys " + self.sysykeysInput.text()
            if self.appswitchInput.text().strip():
                cmd = cmd + "  --pct-appswitch " + self.appswitchInput.text()
            if self.anyeventInput.text().strip():
                cmd = cmd + "  --pct-anyevent " + self.anyeventInput.text()
            if self.pinchInput.text().strip():
                cmd = cmd + "  --pct-pinchzoom " + self.pinchInput.text()
            if self.screenInput.text().strip():
                cmd = cmd + "  --pct-rotation " + self.screenInput.text()
            if self.keyboardInput.text().strip():
                cmd = cmd + "  --pct-flip " + self.keyboardInput.text()
        except:
            pass
        # --ignore-crashes：用于指定当应用程序崩溃时（Force& Close错误），Monkey是否停止运行。如果使用此参数，即使应用程序崩溃，Monkey依然会发送事件，直到事件计数完成
        # --ignore-timeouts：用于指定当应用程序发生ANR（Application No Responding）错误时，Monkey是否停止运行。如果使用此参数，即使应用程序发生ANR错误，Monkey依然会发送事件，直到事件计数完成。
        cmd = cmd + " --ignore-crashes --ignore-timeouts  --monitor-native-crashes"
        return cmd


    def run_command(self,cmd):
        # 执行monkey命令
        try:
            f = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=False)
            while f.poll() is None:
                line = f.stdout.readline()
                line = line.strip()
                if line:
                    self.logger.info("info")
                    self.logger.info(line)
            if f.returncode == 0:
                self.logger.info("命令执行成功")
            else:
                self.logger.error("命令执行失败")
        except:
            pass

    # 获取aapt路径
    def get_aapt(self):
        if "ANDROID_HOME" in os.environ:
            root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
            for path, subdir, files in os.walk(root_dir):
                if "aapt.exe" in files:
                    return os.path.join(path, "aapt.exe")
        else:
            return "ANDROID_HOME not exist"



class Log(object):
    """
    # 日志
    """
    def __init__(self):
        self.file_exists()
        self.logname = project_path + "\\" + 'Log\\'+ time.strftime('%Y-%m-%d') + '.log'
        print(self.logname)

    def print_console(self, level, message):
        # 创建一个log
        logger = logging.getLogger(__name__)
        # 设置日志级别
        logger.setLevel(logging.DEBUG)

        # 创建一个handler,用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s- %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给log添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warring':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)

        logger.removeHandler(fh)
        logger.removeHandler(ch)

    def debug(self, message):
        self.print_console('debug', message)

    def info(self, message):
        self.print_console('info', message)

    def warring(self, message):
        self.print_console('warring', message)

    def error(self, message):
        self.print_console('error', message)

    # 判断日志路径是否存在，不存在则创建
    def file_exists(self):
        if os.path.exists(project_path+ "\\" + 'Log'):
            print("目录存在")
            pass
        else:
            os.makedirs(project_path + "\\" + 'Log')
            print("目录不存在，创建")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.mainUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())