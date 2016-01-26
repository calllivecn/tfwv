#coding=utf-8



import tkinter as tk



win=tk.Tk(className='Place()')

font1=tk.font.Font(size=72)

bg_img=tk.PhotoImage(file='image/background.png')

l_bg=tk.Label(win,text='背景上的文字',font=font1,image=bg_img,compound='center')

l_bg.place(relx=0.5,rely=0.5,anchor='center')

l1=tk.Label(win,text='label-1',font=font1)

l1.place(relx=0.0,rely=0.0)#,anchor='center')



win.mainloop()

