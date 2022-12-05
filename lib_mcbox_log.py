import datetime


def outlog(lv,msg):
    if lv == 0:
        t = str(datetime.datetime.now())
        text = '[Log] [time:' + t + ']' + ' ' + msg + '\n'
        filename = t[0:10] + '.log'
        with open(filename, 'a') as f:
            f.write(text)
    if lv == 1:
        t = str(datetime.datetime.now())
        text = '[Warn] [time:' + t + ']' + ' ' + msg + '\n'
        filename = t[0:10] + '.log'
        with open(filename, 'a') as f:
            f.write(text)
    if lv == 2:
        t = str(datetime.datetime.now())
        text = '[Error] [time:' + t + ']' + ' ' + msg + '\n'
        filename = t[0:10] + '.log'
        with open(filename, 'a') as f:
            f.write(text)
    if lv == 3:
        t = str(datetime.datetime.now())
        text = '[Error!] [time:' + t + ']' + ' Stop! ' + msg + '\n'
        filename = t[0:10] + '.log'
        with open(filename, 'a') as f:
            f.write(text)
        exec('import sys;sys.exit(1)')
def __main__():
    print('mcbox - lib  ver=0.0.1')

if __name__ == "__main__":
    __main__()