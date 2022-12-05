import os

if os.path.exists('i18n.flag'):
    with open('i18n.flag') as f:
        text = f.read()
    #Todo: 打开对应的index文件 如en语言打开 en_index.html 在nwjs.