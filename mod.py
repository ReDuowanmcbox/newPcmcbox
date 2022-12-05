import time
def logout(text='null',lv=0):
    if lv == 0:
        print('[Log] Time is ' + str(int(time.time())) + text)
    elif lv == 1:
        print('[Warn] Time is ' + str(int(time.time())) + text)
    elif lv == 2:
        print('[Error] Time is ' + str(int(time.time())) + text)
    elif lv == 3:
        print('[Error] Stop. Time is ' + str(int(time.time())) + text)
        exec('import sys;sys.exit(1)')
        