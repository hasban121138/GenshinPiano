import sys
from memory_pic import hutao_ico
from base64 import b64decode
from PyQt5.QtWidgets import QApplication
from mainUI import MainUI

if __name__ == "__main__":
    image = open('hutao.ico', 'wb')
    image.write(b64decode(hutao_ico))
    image.close()
    app = QApplication(sys.argv)
    index = MainUI()
    index.show()
    sys.exit(app.exec_())
