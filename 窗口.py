#!/usr/bin/env python3
#coding=utf-8


import tkinter as tk

from tkinter import ttk

win=tk.Tk(className='窗口')

win.geometry('800x600+0+0')

win.minsize(800,600)

frame1=tk.Frame(win,background='#afaffa')



frame2=tk.Frame(frame1,background='#aa8822')
frame3=tk.Frame(win,background='#114488')
frame4=tk.Frame(win,background='#364865')



frame1.place(relx=0.0,rely=0.0,relwidth=0.7,relheight=1.0)
frame2.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.3)
frame3.place(relx=0.7,rely=0.0,relwidth=0.3,relheight=0.6)

T1=tk.Text(frame3,wrap='char')
T1.pack(expand=1,fill='both')

frame4.place(relx=0.7,rely=0.6,relwidth=1,relheight=0.4)







win.mainloop()
