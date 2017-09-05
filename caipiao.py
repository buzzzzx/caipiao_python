from tkinter import *
import random

class Caipiao:
    def __init__(self, root):
        frames = [Frame() for i in range(4)]
        for i in range(4):
            frames[i] = Frame(root)
            frames[i].pack()

        self.button1 = Button(frames[0], text='双色球', fg='red', width=20, command=self.creatDouble)
        self.button1.pack(side=LEFT)

        self.button2 = Button(frames[1], text='大乐透', fg='blue', width=20, command=self.creatDaLeTou)
        self.button2.pack(side=LEFT)

        self.button3 = Button(frames[2], text='清空', width=20, command=self.clearall)
        self.button3.pack()

        self.text = Text(frames[3], width=53, height=15)
        self.scroll = Scrollbar(frames[3], width=4, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT)

    def clearall(self):
        self.text.delete('1.0', END)

    def creatRandom(self, rangeSize, arrSize):
        arrs = [0 for i in range(0, arrSize)]
        rangeArrs = [x + 1 for x in range(rangeSize)]
        for i in range(len(arrs)):
            arrs[i] = rangeArrs[random.randint(0, len(rangeArrs) - 1)]
            rangeArrs.remove(arrs[i])
        arrs.sort()
        return arrs

    def creatDouble(self):
        redball = self.creatRandom(33, 6)
        blueball = random.randint(1, 16)
        ball_str = ''
        for i in redball:
            ball_str = ball_str + str(i) + " "
        ball_str = ball_str + '|' + str(blueball) + '\n'
        self.text.insert(1.0, ball_str)

    def creatDaLeTou(self):
        beforeArea = self.creatRandom(35, 5)
        afterArea = self.creatRandom(12, 2)

        ballstr = ''
        for i in beforeArea:
            ballstr = ballstr + str(i) + ' '
        ballstr = ballstr + '|'
        for i in afterArea:
            ballstr = ballstr + str(i) + ' '
        ballstr = ballstr + '\n'

        self.text.insert(1.0, ballstr)


root = Tk()
xuanhao = Caipiao(root)
root.title("朱欣彩票机选器（一定中！！！）")
root.mainloop()

