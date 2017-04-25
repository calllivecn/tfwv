#!/usr/bin/env python3
#coding=utf-8


import time
import tkinter.ttk as ttk

import tkinter as tk

def winxy(win,w,h):
	display_w=win.winfo_screenwidth()
	display_h=win.winfo_screenheight()
	win_x= (display_w - w) //2
	win_y= (display_h - h) //2
	win.geometry('{}x{}+{}+{}'.format(w,h,win_x,win_y))

def test():
	print(time.ctime())


def createlabel(event):
	global win
	l=ttk.Label(win,text='test func')
	l.grid()

def changeLabel(event):
	global l2
	l2['text']='change: {}'.format(time.ctime())
	

h=True
def nmth(event):
	global l1,h
	if h: 
		l1.pack(side='bottom')#grid(row=1,column=0)
		h=False
	else:
		l1.pack(side='top')#grid(row=0,column=0)
		h=True

win=tk.Tk(className='潜江千分')

winxy(win,800,600)


#frame.pack(expand=tk.YES,ipady=0,ipadx=0,padx=0,pady=0,side=tk.TOP)

bg=tk.PhotoImage(file='image/background.png')
#ttk.Label(frame,image=bd).pack(ipadx=0,ipady=0,padx=0,pady=0)

#frame.pack(ipady=0,ipadx=0)
bg_canvas=tk.Canvas(win,width=800,height=600)
bg_canvas.create_image(0,0,image=bg,anchor='center')
bg_canvas.pack(side='top',expand=1,fill='both')

img1=tk.PhotoImage(file='image/2.png')
img2=tk.PhotoImage(file='image/lv.png')

frame=ttk.Frame(bg_canvas,width=100,height=50)

#win.iconbitmap(img)
#win.geometry('400x300+400+200')
#win.geometry('400x300')

l1=ttk.Label(frame,text='label',image=img1)
l2=ttk.Label(frame,text='label')#,image=img2)
l1.bind('<Button-1>',nmth)
l2.bind('<Button-1>',changeLabel)
#l1.grid(row=2,column=2)
#l2.grid(row=10,column=10,sticky='W')
l1.pack(anchor='w')
b1=ttk.Button(frame,text='Button1',command=test)
b1.pack(anchor='e',expand=1)
frame.pack(side='top',ipady=0,ipadx=0,expand=1,fill='both')
win.mainloop()




## function()

