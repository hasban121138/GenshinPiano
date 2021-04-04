from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui, QtCore
from Ui_about import Ui_About
from Ui_use import Ui_Use


class AboutUI(Ui_About, QDialog):
    def __init__(self):
        super(AboutUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('关于')
        self.setWindowIcon(QtGui.QIcon('hutao.ico'))
        self.logo.setPixmap(QtGui.QPixmap("hutao.ico"))
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.aboutText.setOpenExternalLinks(True)


class UseUI(Ui_Use, QDialog):
    def __init__(self):
        super(UseUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('使用说明')
        self.setWindowIcon(QtGui.QIcon('hutao.ico'))
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.useText.setOpenExternalLinks(True)
