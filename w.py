#!/usr/bin/env python3
#coding=utf-8



import tkinter as tk


def WH(win,w,h):
	#root.withdraw()    #hide window
	screen_width = win.winfo_screenwidth()
	screen_height = win.winfo_screenheight()# - 100    #under windows, taskbar may lie under the screen
	#root.resizable(False,False)
 
	#add some widgets to the root window...
	#root.update_idletasks()
	#root.deiconify()    #now window size was calculated
	#root.withdraw()     #hide window again
	x=screen_width//2 - w//2
	y=screen_height//2 - h//2
	win.geometry('{}x{}+{}+{}'.format(w,h,x,y ))    #center window on desktop
	#root.deiconify()


win=tk.Tk()

img1=tk.PhotoImage(file='image/1.png')
img2=tk.PhotoImage(file='image/2.png')

frame1=tk.Frame(win,width=100,height=200)
frame1.pack(side='left',expand=1,fill='both',ipadx=0,ipady=0)

tk.Label(frame1,image=img1).pack(ipadx=0,ipady=0)


frame2=tk.Frame(win,width=200,height=200)
frame2.pack(side='left',expand=1,fill='both',ipadx=0,ipady=0)

tk.Label(frame2,image=img2).pack(ipadx=0,ipady=0)


frame3=tk.Frame(win,width=100,height=200)
frame3.pack(side='right',expand=1,fill='both',ipadx=0,ipady=0)

tk.Label(frame3,image=img1).pack(ipadx=0,ipady=0)

WH(win,400,300)
#root.maxsize(800,600)
#win.minsize(200,150)
win.mainloop()

