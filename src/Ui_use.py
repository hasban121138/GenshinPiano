# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Use(object):
    def setupUi(self, Use):
        Use.setObjectName("Use")
        Use.resize(620, 474)
        self.useText = QtWidgets.QLabel(Use)
        self.useText.setGeometry(QtCore.QRect(10, 0, 581, 461))
        self.useText.setObjectName("useText")

        self.retranslateUi(Use)
        QtCore.QMetaObject.connectSlotsByName(Use)

    def retranslateUi(self, Use):
        _translate = QtCore.QCoreApplication.translate
        Use.setWindowTitle(_translate("Use", "Dialog"))
        self.useText.setText(_translate("Use", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff131f;\">注意:</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ff131f;\">由于是按键模拟器,无法保证完全安全,请谨慎使用</span></p><p><a href=\"https://www.bilibili.com/video/BV15i4y1N7A7\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">使用说明</span></a><span style=\" font-size:14pt; font-weight:600;\">:</span></p><p><span style=\" font-size:14pt; font-weight:600;\">使用管理员身份运行</span></p><p><span style=\" font-size:14pt; font-weight:600;\">在输入框中输入字符，点击开始即可弹奏</span></p><p><span style=\" font-size:14pt; font-weight:600;\">使用括号(英文)表示和弦，例如:(AE)表示同时按下AE</span></p><p><span style=\" font-size:14pt; font-weight:600;\">延迟为每个音符的停顿时长，单位:毫秒</span></p><p><span style=\" font-size:14pt; font-weight:600;\">编辑-&gt;启用单音延迟开启单音延迟功能，$表示延迟的单位时长</span></p><p><span style=\" font-size:14pt; font-weight:600;\">例如：</span></p><p><span style=\" font-size:14pt; font-weight:600;\">A$B 表示按下A延迟1个单位时间后按下B</span></p><p><span style=\" font-size:14pt; font-weight:600;\">$$$ 表示延长3个单位时间</span></p><p><span style=\" font-size:14pt; font-weight:600;\">$3 表示延长3个单位时间，同$$$</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ff131f;\">请尽可能不要输入奇怪的东西防止出现Bug</span></p></body></html>"))

