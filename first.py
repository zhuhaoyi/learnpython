from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

exit()
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()



exit()
import os

print(os.getppid())
pid = os.fork()
print(pid)



exit()
teemo=[]
n=1
while n<=100:
    teemo.append(n)
    n=n+3
print(teemo[3:8])


exit()
for x in range(0, 3):
    def age(num):
        if num > 18:
            print('old')
        elif num < 18:
            print('young')
        else:
            print('i don\'t konw')

    text = input("type your age\nage:")
    text = int(text)
    age(text)

print('完毕')

print(json._default_decoder)

def teemo(*num):
    for n in num:
        print(n)

teemo(1,2,3)

