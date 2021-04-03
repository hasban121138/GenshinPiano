from memory_pic import *
from base64 import b64decode

def getLogo():
    image = open('hutao.ico', 'wb')
    image.write(b64decode(hutao_ico))
    image.close()