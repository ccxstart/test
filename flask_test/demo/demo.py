"""
@coding: utf-8
@author: 星辰
@date: 2023/10/11 15:02
"""
import random
import tkinter as tk
import threading


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('哈哈哈哈哈哈')
    window.geometry('210x50' + '+' + str(a) + '+' + str(b))
    tk.Label(window, text='你是傻逼', bg='pink', font=('楷体', 17), width=16, height=3).pack()
    window.mainloop()


threads = []
for i in range(100):
    t = threading.Thread(target=dow)
    threads.append(t)
    t.start()

