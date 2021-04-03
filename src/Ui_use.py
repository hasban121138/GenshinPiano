# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\hasan\GenshinPiano\res\ui\use.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Use(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 328)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 461, 321))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">注意:</span></p><p><span style=\" font-size:14pt; font-weight:600;\">由于是按键模拟器,无法保证完全安全,请谨慎使用</span></p><p><span style=\" font-size:14pt; font-weight:600;\">使用说明:</span></p><p><span style=\" font-size:14pt; font-weight:600;\">使用管理员身份运行</span></p><p><span style=\" font-size:14pt; font-weight:600;\">在输入框中输入字符，点击开始即可弹奏</span></p><p><span style=\" font-size:14pt; font-weight:600;\">使用括号(英文)表示和弦</span></p><p><span style=\" font-size:14pt; font-weight:600;\">例如:(AE)表示同时按下AE</span></p><p><span style=\" font-size:14pt; font-weight:600;\">延迟为每个音符的停顿时长，单位:毫秒</span></p><p><span style=\" font-size:14pt; font-weight:600;\">请尽可能不要输入奇怪的东西防止出现Bug</span></p></body></html>"))

