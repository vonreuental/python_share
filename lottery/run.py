import random
import threading
import time
import tkinter

from lottery.wx_bot import WxBot

# 初始化窗口
root = tkinter.Tk()
root.title("随机名单")
root.geometry('500x500+400+200')
root.resizable(False, False)
root.flag = True

# 三个Lable标签
first = tkinter.Label(root, text='', font=("宋体", 18, "normal"))
first.place(x=180, y=100, width=150, height=100)

second = tkinter.Label(root, text='', font=("宋体", 28, "normal"))
second['fg'] = 'red'
second.place(x=180, y=200, width=150, height=100)

third = tkinter.Label(root, text='', font=("宋体", 16, "normal"))
third.place(x=180, y=300, width=150, height=100)

bot = WxBot()
member = bot.get_menber_name('创新业务研发小微')


def switch():
    root.flag = True
    while root.flag:
        i = random.randint(0, len(member) - 1)
        first['text'] = second['text']
        second['text'] = third['text']
        third['text'] = member[i]
        time.sleep(0.05)


# 开始按钮
def butStartClick():
    t = threading.Thread(target=switch)
    t.start()


btnStart = tkinter.Button(root, text='开始', command=butStartClick)
btnStart.place(x=30, y=30, width=80, height=20)


# 结束按钮
def btnStopClick():
    root.flag = False
    member.remove(second['text'])


butStop = tkinter.Button(root, text='停止', command=btnStopClick)
butStop.place(x=160, y=30, width=80, height=20)

# 启动主程序
root.mainloop()
