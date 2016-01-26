#!/usr/bin/env python3
#coding=utf-8


import time

import tkinter as tk

from tkinter import ttk

def move(event):
    print('Ecvent : ',event)

win=tk.Tk(className='test  window')

background=tk.PhotoImage(file='image/background.png')

label_bg=tk.Label(win,image=background)

label_bg.pack(expand=1,fill='both')#,ipadx='5m',ipady='5m')

#win.geometry('800x600')

win.minsize(400,300)

frame1=tk.Frame(label_bg)

label1=tk.Label(frame1,text='label-1')#,bg='#aaff00')

label2=tk.Label(frame1,text='label-2',bg='#123363')

label3=tk.Label(frame1,text='label-3',bg='#0000ff')

label4=tk.Label(label_bg,text='label-4',bg='#aa0000')

label1.bind('<Button-1>',move,'argumnet???')


frame1.pack(expand=1)#()

label1.pack(side='top',anchor='w')

label2.pack(side='right',fill='y')

label3.pack(side='top',expand=1)



label4.pack(side='bottom',fill='both')

'''
frame1.pack(side='left',fill='y',padx='5m',pady='5m')#side='left',expand=1,anchor='n')

frame2.pack(side='top',after=frame1)

frame3.pack(side='right',after=frame1)

frame4.pack(side='top',expand=1,fill='both',padx='5m',pady='5m')
'''

'''
label2=tk.Label(label1,text='label-2')

label2.pack()

'''




'''
frame1.pack(side='left')#,anchor='w')

frame2.pack(side='left')#,anchor='s')

frame3.pack(side='left')#,anchor='center')

frame4.pack(side='top')

frame1.grid(sticky='nw')

frame2.grid(sticky='n')

frame3.grid()

frame4.grid()
'''
win.mainloop()

