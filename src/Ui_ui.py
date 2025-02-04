# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 521)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.noteContainer = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteContainer.setGeometry(QtCore.QRect(20, 10, 700, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.noteContainer.setFont(font)
        self.noteContainer.setObjectName("noteContainer")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(645, 440, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setObjectName("startBtn")
        self.noteDelaySplitter = QtWidgets.QSplitter(self.centralwidget)
        self.noteDelaySplitter.setGeometry(QtCore.QRect(230, 440, 205, 20))
        self.noteDelaySplitter.setOrientation(QtCore.Qt.Horizontal)
        self.noteDelaySplitter.setObjectName("noteDelaySplitter")
        self.noteDelayText = QtWidgets.QLabel(self.noteDelaySplitter)
        self.noteDelayText.setObjectName("noteDelayText")
        self.noteDelay = QtWidgets.QLineEdit(self.noteDelaySplitter)
        self.noteDelay.setObjectName("noteDelay")
        self.unitMs_2 = QtWidgets.QLabel(self.noteDelaySplitter)
        self.unitMs_2.setObjectName("unitMs_2")
        self.gloablDelaySplitter = QtWidgets.QSplitter(self.centralwidget)
        self.gloablDelaySplitter.setGeometry(QtCore.QRect(20, 440, 181, 20))
        self.gloablDelaySplitter.setOrientation(QtCore.Qt.Horizontal)
        self.gloablDelaySplitter.setObjectName("gloablDelaySplitter")
        self.delayText = QtWidgets.QLabel(self.gloablDelaySplitter)
        self.delayText.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delayText.sizePolicy().hasHeightForWidth())
        self.delayText.setSizePolicy(sizePolicy)
        self.delayText.setObjectName("delayText")
        self.gloablDelay = QtWidgets.QLineEdit(self.gloablDelaySplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gloablDelay.sizePolicy().hasHeightForWidth())
        self.gloablDelay.setSizePolicy(sizePolicy)
        self.gloablDelay.setObjectName("gloablDelay")
        self.unitMs = QtWidgets.QLabel(self.gloablDelaySplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unitMs.sizePolicy().hasHeightForWidth())
        self.unitMs.setSizePolicy(sizePolicy)
        self.unitMs.setObjectName("unitMs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 23))
        self.menubar.setObjectName("menubar")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.edit = QtWidgets.QMenu(self.menubar)
        self.edit.setObjectName("edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionuse = QtWidgets.QAction(MainWindow)
        self.actionuse.setObjectName("actionuse")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsaveAs = QtWidgets.QAction(MainWindow)
        self.actionsaveAs.setObjectName("actionsaveAs")
        self.actiongloablDelay = QtWidgets.QAction(MainWindow)
        self.actiongloablDelay.setObjectName("actiongloablDelay")
        self.actionnoteDelay = QtWidgets.QAction(MainWindow)
        self.actionnoteDelay.setCheckable(True)
        self.actionnoteDelay.setObjectName("actionnoteDelay")
        self.help.addAction(self.actionuse)
        self.help.addAction(self.actionabout)
        self.file.addAction(self.actionopen)
        self.file.addSeparator()
        self.file.addAction(self.actionsave)
        self.file.addAction(self.actionsaveAs)
        self.edit.addAction(self.actionnoteDelay)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.edit.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "开始"))
        self.noteDelayText.setText(_translate("MainWindow", "单音延迟"))
        self.unitMs_2.setText(_translate("MainWindow", "毫秒"))
        self.delayText.setText(_translate("MainWindow", "延迟"))
        self.unitMs.setText(_translate("MainWindow", "毫秒"))
        self.help.setTitle(_translate("MainWindow", "帮助"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.edit.setTitle(_translate("MainWindow", "编辑"))
        self.actionuse.setText(_translate("MainWindow", "使用说明"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionsave.setText(_translate("MainWindow", "保存"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionopen.setText(_translate("MainWindow", "打开"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionsaveAs.setText(_translate("MainWindow", "另存为"))
        self.actionsaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actiongloablDelay.setText(_translate("MainWindow", "gloablDelay"))
        self.actionnoteDelay.setText(_translate("MainWindow", "启用单音延迟"))

