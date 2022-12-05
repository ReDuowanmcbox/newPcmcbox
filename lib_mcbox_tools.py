import os
import urllib.request
import lib_mcbox_log
def mcboxExec(shell):
    t = os.popen(shell)
    t = t.read()
    return t 
def checkUpDate():
    t = urllib.request.urlopen('http://101.43.48.113:1025/')
    onlineVers = t.read()
    onlineVer = onlineVers.split('|')
    return onlineVer
def upDate():
    os.system('powershell rm setup.exe')
    f = open('setup.exe','wb')
    fb = urllib.request.urlopen('http://101.43.48.113/pcsetup.exe')
    f.write(fb.data)
    f.close()
    os.system('start setup.exe')
    lib_mcbox_log.logout('Update is over',0)
def getOnlineMsg():
    t = urllib.request.urlopen('http://101.43.48.113/api/msg/getmsg.php')
    t = t.read()
    return t