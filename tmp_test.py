#/usr/bin/env python3
#coding=utf-8

import random

import tkinter as tk

from tkinter import ttk

root = tk.Tk()

root.geometry('400x300+100+100')

#root.overrideredirect(True)
root.attributes("-alpha", 0.3)#窗口透明度70 %

root.config(background='#000000')



f1=tk.Frame(root,bg='#123452')

f1.place(x=0,y=0,relwidth=1,relheight=0.1)

f2=tk.Frame(root,bg='#223423')

f2.place(x=0,rely=0.1,relwidth=1,relheight=0.9)


f2_f1=tk.Frame(f2)

sum_p=[]
def p():
    global W,H
    for i in range(random.randrange(0,54)):
        p=tk.Label(text='两个',width=2,height=2,wraplength=1)
        W=p.winfo_width()
        H=p.winfo_y()
        sum_p.append(p)
        print(W,H)

def sort(w,h):
    global sum_p
    x=w//W #两个字符宽度
    
    y=len(sum_p)//H#两个字符高度
    if len(sum_p)%H >0:
        y+=1
    
    tail=0
    for i in range(y):
        f=tk.Frame(f2_f1)
        f.pack(fill='x')
        for j in range(x):
            sum_p[0].pack(in_=f,side='left')
            tail+=1
    

FLAG=[10,400,300]
def change(event):
    global FLAG
    if FLAG[0]==0 and ( FLAG[1] != event.width or FLAG[2] != event.height ):
        FLAG[0]=10
        FLAG[1],FLAG[2]=event.width,event.height
        print(FLAG)

    FLAG[0]-=1


root.bind('<Configure>',change)

p()
sort(FLAG[1],FLAG[2])


root.mainloop()
