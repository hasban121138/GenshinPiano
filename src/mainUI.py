from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui
from Ui_ui import Ui_MainWindow
from time import sleep
from pynput.keyboard import Controller
from menuUI import AboutUI, UseUI

verify = [
    'q',
    'w',
    'e',
    'r',
    't',
    'y',
    'u',
    'a',
    's',
    'd',
    'f',
    'g',
    'h',
    'j',
    'z',
    'x',
    'c',
    'v',
    'b',
    'n',
    'm',
]


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__()
        self.keyboard = Controller()
        self.setupUi(self)
        self.setWindowTitle('原神风物琴自动弹奏工具')
        self.setWindowIcon(QtGui.QIcon('hutao.ico'))
        self.setFixedSize(self.width(), self.height())
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.pushButton.clicked.connect(self._onStart)

        self.actionabout.triggered.connect(self._about)
        self.aboutUI = AboutUI()

        self.actionuse.triggered.connect(self._use)
        self.useUI = UseUI()

    def _onStart(self):
        text = self.plainTextEdit.toPlainText()
        delay = self.lineEdit.text()
        textlen = len(text)
        if (textlen == 0 or delay == ''):
            return
        bracketsFlage = False       # 括号
        waitingNote = set(())       # 和弦音符
        delay = int(delay)
        sleep(3)
        for curText in text:
            print(curText)
            if (curText == '('):
                if (bracketsFlage):  # 存在左括号又有左括号错误 直接消耗音符
                    print(waitingNote)
                    bracketsFlage = False
                    for _ in waitingNote:
                        self.keyboard.press(_)
                        self.keyboard.release(_)
                        print(_)
                    sleep(delay / 1000)
                    waitingNote.clear()
                else:       # 正常的左括号
                    bracketsFlage = True
            elif (curText == ')'):
                if (not bracketsFlage and not len(waitingNote)):  # 错误的第一次右括号
                    bracketsFlage = True
                else:  # 消耗音符
                    bracketsFlage = False
                    for _ in waitingNote:
                        self.keyboard.press(_)
                        self.keyboard.release(_)
                        print(_)
                    sleep(delay / 1000)
                    waitingNote.clear()
            elif (str.isalpha(curText) and curText.lower() in verify):
                if (not bracketsFlage):
                    self.keyboard.press(curText.lower())
                    self.keyboard.release(curText.lower())
                    sleep(delay / 1000)
                else:       # 和弦
                    waitingNote.add(curText.lower())

    def _use(self):
        self.useUI.show()

    def _about(self):
        self.aboutUI.show()
