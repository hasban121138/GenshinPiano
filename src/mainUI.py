import os
import re
from time import sleep
from PyQt5 import QtGui, QtWidgets
from pynput.keyboard import Controller
from Ui_ui import Ui_MainWindow
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

noteDelayMark = '$'


class MainUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__()
        self.keyboard = Controller()
        self.saved = True
        self.notePath = os.getcwd()
        self.filePath = ''
        self.title = '原神风物琴自动弹奏工具'
        self.setupUi(self)
        self.setWindowTitle(self.title + ' - ' + '未命名')
        self.setWindowIcon(QtGui.QIcon('hutao.ico'))
        self.setFixedSize(self.width(), self.height())
        self.gloablDelay.setValidator(QtGui.QIntValidator())

        self.startBtn.clicked.connect(self._onStart)
        self.noteDelay.setValidator(QtGui.QIntValidator())
        self.noteDelaySplitter.hide()
        self.noteContainer.textChanged.connect(self._fileChange)
        self.gloablDelay.textChanged.connect(self._fileChange)
        self.noteDelay.textChanged.connect(self._fileChange)

        self.actionnoteDelay.triggered.connect(self._noteDelayShow)
        self.actionopen.triggered.connect(self._onOpen)
        self.actionsave.triggered.connect(self._save)
        self.actionsaveAs.triggered.connect(self._saveAs)

        self.actionabout.triggered.connect(self._about)
        self.aboutUI = AboutUI()

        self.actionuse.triggered.connect(self._use)
        self.useUI = UseUI()

    def _onStart(self):
        text = self.noteContainer.toPlainText()
        delay = self.gloablDelay.text().strip()
        noteDelay = self.noteDelay.text().strip()
        noteDelayFlage = self.actionnoteDelay.isChecked()
        textlen = len(text)

        if (textlen == 0 or delay == ''):  # 正常延迟
            return
        if (noteDelayFlage):  # 单音延迟
            if (noteDelay == ''):
                return
            else:
                noteDelay = int(noteDelay)

        bracketsFlage = False  # 括号
        waitingNote = set(())  # 和弦音符
        delay = int(delay)
        waitingTime = 0
        i = 0

        sleep(3)
        while True:
            if (i >= textlen):
                break
            curText = text[i]
            i = i + 1

            if (curText == '(' or curText == '（'):
                if (bracketsFlage):  # 存在左括号又有左括号错误 直接消耗音符
                    bracketsFlage = False
                    for _ in waitingNote:
                        self.keyboard.press(_)
                        self.keyboard.release(_)
                    waitingNote.clear()
                    if (i < textlen and
                            text[i] != noteDelayMark):  # 如果下一个是$表示单音延迟否则正常延迟
                        sleep(delay / 1000)
                else:  # 正常的左括号
                    bracketsFlage = True

            elif (curText == ')' or curText == '）'):
                if (not bracketsFlage and not len(waitingNote)):  # 错误的第一次右括号
                    bracketsFlage = True
                else:  # 消耗音符
                    bracketsFlage = False
                    for _ in waitingNote:
                        self.keyboard.press(_)
                        self.keyboard.release(_)
                    waitingNote.clear()
                    if (i < textlen and
                            text[i] != noteDelayMark):  # 如果下一个是$表示单音延迟否则正常延迟
                        sleep(delay / 1000)

            elif (str.isalpha(curText) and curText.lower() in verify):
                if (not bracketsFlage):
                    self.keyboard.press(curText.lower())
                    self.keyboard.release(curText.lower())
                    if (i < textlen and
                            text[i] != noteDelayMark):  # 如果下一个是$表示单音延迟否则正常延迟
                        sleep(delay / 1000)
                else:  # 和弦
                    waitingNote.add(curText.lower())

            #     开启单音延迟          不做括号中              $开始
            elif (noteDelayFlage and (not bracketsFlage)
                  and curText == noteDelayMark):  # 单音延迟
                if (i >= textlen):
                    break
                nextText = text[i]  # 提前读下一个数据
                if (nextText == noteDelayMark):  # $+$ 时间+1 此处的1为当前的$
                    waitingTime = waitingTime + 1
                elif (str.isalpha(nextText)):  # $+字母 释放时间
                    waitingTime = waitingTime + 1
                    sleep(waitingTime * noteDelay / 1000)
                    waitingTime = 0
                elif (str.isdigit(nextText)):  # $+数字 继续下读
                    tmp = nextText
                    newI = i + 1
                    while True:
                        # 只要下一个不是数字就停止读入 释放
                        if (newI >= textlen or (not str.isdigit(text[newI]))):
                            i = newI
                            waitingTime = waitingTime + int(tmp)
                            sleep(waitingTime * noteDelay / 1000)
                            waitingTime = 0
                            break
                        if (str.isdigit(text[newI])):  # 数字添加
                            tmp = tmp + text[newI]
                        newI = newI + 1

    def _use(self):
        self.useUI.show()

    def _about(self):
        self.aboutUI.show()

    def _noteDelayShow(self, checked):
        if (checked):
            self.noteDelaySplitter.show()
        else:
            self.noteDelaySplitter.hide()
        self._fileChange()

    def _fileChange(self):
        if (self.saved):
            self.setWindowTitle(self.windowTitle() + '*')
            self.saved = False

    def save(self):
        delay = self.gloablDelay.text()
        noteDelay = self.noteDelay.text()
        noteDelayFlage = self.actionnoteDelay.isChecked()
        text = self.noteContainer.toPlainText()

        if(not len(text.strip())):
            return
        try:
            with open(self.filePath, 'w', encoding='utf-8') as noteFile:
                noteFile.write('#delay:' + delay + '\n')
                noteFile.write('#noteDelay:' + noteDelay + '\n')
                noteFile.write('#noteDelayFlage:' + str(noteDelayFlage) + '\n')
                noteFile.write(text + '\n')
            self.saved = True
            self.setWindowTitle(self.windowTitle()[0:-1])
        except Exception:
            self.noteContainer.clear()
            self.noteContainer.appendPlainText('文件保存失败')

    def _save(self):  # 保存
        if (self.saved):
            return

        if (self.filePath == ''):  # 文件没有路径添加
            fullFileName, fileType = QtWidgets.QFileDialog.getSaveFileName(
                self, '保存文件', self.notePath, '文本文件(*.txt)')
            if (fullFileName == ''):
                return

            self.filePath = fullFileName
            filePath, fileName = os.path.split(fullFileName)
            self.notePath = filePath
            self.setWindowTitle(self.title + '  -  ' + fileName + '*')

        self.save()  # 已经有了路径

    def _saveAs(self):  # 另存为 打开文件管理器
        fullFileName, fileType = QtWidgets.QFileDialog.getSaveFileName(
            self, '保存文件', self.notePath, '文本文件(*.txt)')
        if (fullFileName == ''):
            return

        self.filePath = fullFileName
        filePath, fileName = os.path.split(fullFileName)
        self.notePath = filePath
        self.setWindowTitle(self.title + '  -  ' + fileName + '*')
        self.save()

    def _onOpen(self):
        fullFileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
            self, '选取文件', self.notePath, 'All Files(*);;文本文件(*.txt)')
        if (not fullFileName):
            return

        filePath, fileName = os.path.split(fullFileName)
        self.notePath = filePath
        self.filePath = fullFileName
        self.noteContainer.clear()
        self.actionnoteDelay.setChecked(False)
        self.noteDelaySplitter.hide()
        self.gloablDelay.setText('')
        self.noteDelay.setText('')

        with open(fullFileName, 'r', encoding='utf-8') as noteFile:
            line = noteFile.readline()
            while line:
                if (line.startswith('#delay:')):
                    reDelay = re.match(r'#delay:(\d*)', line, re.I)
                    self.gloablDelay.setText(reDelay.group(1))

                elif (line.startswith('#noteDelay:')):
                    reNoteDelay = re.match(r'#noteDelay:(\d*)', line, re.I)
                    self.noteDelay.setText(reNoteDelay.group(1))

                elif (line.startswith('#noteDelayFlage:')):
                    reNoteDelayFlage = re.match(r'#noteDelayFlage:(\w*)', line,
                                                re.I)
                    if (reNoteDelayFlage.group(1) == 'True'):
                        self.actionnoteDelay.setChecked(True)
                        self.noteDelaySplitter.show()
                    elif (reNoteDelayFlage.group(1) == 'False'):
                        self.actionnoteDelay.setChecked(False)
                        self.noteDelaySplitter.hide()
                elif (line == '\n'):
                    pass
                else:
                    self.noteContainer.appendPlainText(line)
                line = noteFile.readline()

        # 和textChange冲突 设置窗口名需在赋值后
        self.saved = True
        self.setWindowTitle(self.title + '  -  ' + fileName)
