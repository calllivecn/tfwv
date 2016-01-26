import tkinter as tk

from tkinter import ttk

def get(event):
    print(user_entry.get())
    user_entry.delete(0,'end')

def clear(event):
    password_entry.delete(0,'end')

win=tk.Tk(className='用户登陆')

#win_root.overrideredirect(1)

win.attributes('-alpha',0.2)

win.propagate(0)
win.resizable(0,0)


'''
img1=tk.PhotoImage(file='image/6.png')

win=tk.Label(win_root)#,image=img1)

win.grid()
'''
user=tk.Label(win,text='用户名：')

password=tk.Label(win,text='密码：')

user_entry=tk.Entry(width=20)

user_entry.bind('<Return>',get)

password_entry=tk.Entry(width=20,show='x')

password_entry.bind('<Return>',clear)

user.grid(row=0,column=0)
user_entry.grid(row=0,column=1,columnspan=2)

password.grid(row=1,column=0)
password_entry.grid(row=1,column=1,columnspan=2)

button1=tk.Button(win,text='登陆',command=lambda :get('nothing'))
button2=tk.Button(win,text='退出',command=win.destroy)

button1.grid(row=2,column=1,sticky='e')
button2.grid(row=2,column=2,sticky='e')


win.mainloop()
