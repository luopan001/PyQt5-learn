#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : .py
# @Author: Luopan
# @Date  : 2018/8/8 14:30
# @Desc  : android，monkey测试辅助小工具。 继承自MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os,re,subprocess
from PyQt5.QtWidgets import QMessageBox

icon_path = r"D://project_pro//PyQt5-learn//icons//android.png"

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.mainUI(self)
        self.retranslateUi(self)
        self.aapt_path = self.get_aapt()

    def mainUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 915)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 30, 647, 725))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.printDeviceInfo = QtWidgets.QPlainTextEdit(self.groupBox)
        self.printDeviceInfo.setObjectName("printDeviceInfo")
        self.verticalLayout.addWidget(self.printDeviceInfo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deviceInfo = QtWidgets.QPushButton(self.groupBox)
        self.deviceInfo.setObjectName("deviceInfo")
        self.horizontalLayout.addWidget(self.deviceInfo)
        self.deviceRst = QtWidgets.QPushButton(self.groupBox)
        self.deviceRst.setObjectName("deviceRst")
        self.horizontalLayout.addWidget(self.deviceRst)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.printAppRoute = QtWidgets.QLineEdit(self.groupBox_2)
        self.printAppRoute.setObjectName("printAppRoute")
        self.horizontalLayout_5.addWidget(self.printAppRoute)
        self.getAppRoute = QtWidgets.QPushButton(self.groupBox_2)
        self.getAppRoute.setObjectName("getAppRoute")
        self.horizontalLayout_5.addWidget(self.getAppRoute)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.appName_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.appName_1.setObjectName("appName")
        self.verticalLayout_3.addWidget(self.appName_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.installBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.installBtn.setObjectName("installBtn")
        self.horizontalLayout_2.addWidget(self.installBtn)
        self.uninstallBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.uninstallBtn.setObjectName("uninstallBtn")
        self.horizontalLayout_2.addWidget(self.uninstallBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.printAppRoute_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.printAppRoute_2.setObjectName("printAppRoute_2")
        self.horizontalLayout_6.addWidget(self.printAppRoute_2)
        self.geiAppRoute_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.geiAppRoute_2.setObjectName("geiAppRoute_2")
        self.horizontalLayout_6.addWidget(self.geiAppRoute_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.printAppInfo = QtWidgets.QTextEdit(self.groupBox_3)
        self.printAppInfo.setObjectName("printAppInfo")
        self.verticalLayout_4.addWidget(self.printAppInfo)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.getAppInfo = QtWidgets.QPushButton(self.groupBox_3)
        self.getAppInfo.setObjectName("getAppInfo")
        self.horizontalLayout_3.addWidget(self.getAppInfo)
        self.appReset = QtWidgets.QPushButton(self.groupBox_3)
        self.appReset.setObjectName("appReset")
        self.horizontalLayout_3.addWidget(self.appReset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.appnameInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.appnameInput.setObjectName("appnameInput")
        self.verticalLayout_8.addWidget(self.appnameInput)
        self.throttleInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.throttleInput.setObjectName("throttleInput")
        self.verticalLayout_8.addWidget(self.throttleInput)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox)
        self.countInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.countInput.setObjectName("countInput")
        self.verticalLayout_8.addWidget(self.countInput)
        self.seedInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.seedInput.setObjectName("seedInput")
        self.verticalLayout_8.addWidget(self.seedInput)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        self.motionInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.motionInput.setObjectName("motionInput")
        self.verticalLayout_8.addWidget(self.motionInput)
        self.trackballInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.trackballInput.setObjectName("trackballInput")
        self.verticalLayout_8.addWidget(self.trackballInput)
        self.navInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.navInput.setObjectName("navInput")
        self.verticalLayout_8.addWidget(self.navInput)
        self.majotnavInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.majotnavInput.setObjectName("majotnavInput")
        self.verticalLayout_8.addWidget(self.majotnavInput)
        self.sysykeysInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.sysykeysInput.setObjectName("sysykeysInput")
        self.verticalLayout_8.addWidget(self.sysykeysInput)
        self.appswitchInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.appswitchInput.setObjectName("appswitchInput")
        self.verticalLayout_8.addWidget(self.appswitchInput)
        self.anyeventInput = QtWidgets.QLineEdit(self.groupBox_4)
        self.anyeventInput.setObjectName("anyeventInput")
        self.verticalLayout_8.addWidget(self.anyeventInput)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.monkeyTestBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.monkeyTestBtn.setObjectName("monkeyTestBtn")
        self.horizontalLayout_4.addWidget(self.monkeyTestBtn)
        self.viewlogBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.viewlogBtn.setObjectName("viewlogBtn")
        self.horizontalLayout_4.addWidget(self.viewlogBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.remark = QtWidgets.QLabel(self.groupBox_5)
        self.remark.setObjectName("remark")
        self.verticalLayout_6.addWidget(self.remark)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
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
        self.installBtn.clicked.connect(self.install_app)
        self.uninstallBtn.clicked.connect(self.uninstall_app)
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
        self.uninstallBtn.setText(_translate("MainWindow", "点击卸载"))
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
        self.trackball.setText(_translate("MainWindow", "轨迹球事件%（trackball）"))
        self.nav.setText(_translate("MainWindow", "基本导航事件%（nav）"))
        self.majornav.setText(_translate("MainWindow", "主要导航事件%（majornav）"))
        self.syskeys.setText(_translate("MainWindow", "系统关键时间%（syskeys）"))
        self.appswitch.setText(_translate("MainWindow", "运行包内activity%(appswitch)"))
        self.anyevent.setText(_translate("MainWindow", "其他类型事件%（anyevent）"))
        self.comboBox.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2"))
        self.monkeyTestBtn.setText(_translate("MainWindow", "执行monkey测试"))
        self.viewlogBtn.setText(_translate("MainWindow", "查看日志"))
        self.groupBox_5.setTitle(_translate("MainWindow", "备注信息"))
        remark_string = "1、环境检查\n1)请首先配置安卓环境（aapt环境）\n2)请安装安卓手机模拟器或者插入真机进行测试，配置好adb\n" \
                        "2、获取应用信息的匹配规则请根据所测app灵活进行调整\n3、开发人员信息\n1) 姓名：luopan\n2）联系方式：XXXXX"
        self.remark.setText(remark_string)

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
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, '选择应用安装包', '/', 'Apk Files (*.apk)')
        self.printAppRoute.setText(self.filename)

    # 应用信息：获取安装包路径，点击应用信息模块的“浏览”按钮
    def get_windows_file_2(self):
        self.filename_1, _ =  QtWidgets.QFileDialog.getOpenFileName(self, '选择应用安装包', '/', 'Apk Files (*.apk)')
        self.printAppRoute_2.setText(self.filename_1)

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
        print(self.printAppRoute_2.text())
        try:
            if self.printAppRoute_2.text() is not None:
                size = round(os.path.getsize(self.printAppRoute_2.text()) / (1024 * 1000), 2)
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
                print(launchable_activity_name)
                return (package_name,version_code,version_name,launchable_activity_name)
        except:
            pass

    # 安装app
    def install_app(self):
        print("111"+self.printAppRoute.text())
        try:
            if self.printAppRoute.text().strip():
                cmd = "adb install " + self.printAppRoute.text()
                print(cmd)
                data = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
                #print(data.stdout.read().decode())
            else:
                QMessageBox.warning(self, "警告", "请先上传安装包", QMessageBox.NoButton)
        except:
            pass

    # 卸载app
    def uninstall_app(self):
        print(self.appName_1.text())
        # 非apk文件：Missing APK file 错误的apk文件：Invalid APK file

    def monkey_test(self):
        print("monkey测试开始")

    def view_log(self):
        print("查看日志")

    # 获取aapt路径
    def get_aapt(self):
        if "ANDROID_HOME" in os.environ:
            root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
            for path, subdir, files in os.walk(root_dir):
                if "aapt.exe" in files:
                    return os.path.join(path, "aapt.exe")
        else:
            return "ANDROID_HOME not exist"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.mainUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())