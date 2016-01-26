#coding=utf-8

import time

import tkinter as tk

from tkinter import ttk



win=tk.Tk(className='grid')

label1=tk.Label(win,text='label-1',background='#00ff00')

label2=tk.Label(win,text='label-2',background='#aaaaaa')

label3=tk.Label(win,text='label-3',bg='#123456')

label1.grid(rowspan=2,columnspan=2)

label2.grid(row=0,column=2,rowspan=2,columnspan=2,sticky='e')

label3.grid()


win.mainloop()
