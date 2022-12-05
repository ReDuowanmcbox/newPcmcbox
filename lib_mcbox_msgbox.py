import tkinter
import tkinter.messagebox

import lib_mcbox_log


def mcbox_showinfo(msg="有一个很恶趣味的开发者,不知道为什么给你发了一个没有内容的提示框"):
    root = tkinter.Tk()
    tkinter.messagebox.showinfo('Re多玩我的世界盒子',msg)
def mcbox_showerror(msg="[E000] 未知错误"):
    root = tkinter.Tk()
    lib_mcbox_log.outlog(2,msg)
    tkinter.messagebox.showerror('Re多玩我的世界盒子',msg)
def mcbox_showwarn(msg="[E000] 未知错误(警告)"):
    root = tkinter.Tk()
    lib_mcbox_log.outlog(1,msg)
    tkinter.messagebox.showwarning('Re多玩我的世界盒子',msg)
def __main__():
    test()
def test():
    mcbox_showinfo('mcbox lib ver=0.0.1')
    mcbox_showerror('这是一条错误消息弹出测试')
    mcbox_showwarn('这是一条警告消息测试.')
    mcbox_showwarn()
    mcbox_showerror()
    mcbox_showinfo()
    mcbox_showinfo('这个开发者一点也不恶趣味，他只是想给你发个提示框')
if __name__ == "__main__":
    __main__()