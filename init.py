import os
import lib_mcbox_log
import lib_mcbox_tools


ver = '1.0.0beta'
try:
    onlineVer = lib_mcbox_tools.checkUpDate()
    if not ver == onlineVer[2]:
        lib_mcbox_tools.upDate()
    lib_mcbox_log.outlog('mcbox is setup.',0)
    onlineMsg = lib_mcbox_tools.getOnlineMsg()
    with open('msg.html','r') as f:
        t        = str(f.read())
        htmlText = t
    with open('msg.html','w') as f:
        f.write(htmlText)
        del(t)
        del(htmlText)
        lib_mcbox_log.outlog('GetOnlineMsg',0)
except:
    pass
lib_mcbox_log.outlog('Starting...',0)
os.system(os.getcwd() + '\\mini-electron.exe')
