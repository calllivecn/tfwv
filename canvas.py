import time
import threading as th
import tkinter as tk

flag=10
def win_change(event):
    global flag
    if flag==0:
        flag=10
        x=event.width
        y=event.height
        print(x,y)
    else:
        flag-=1


win=tk.Tk()

win.bind('<Configure>',win_change)

f=tk.Frame(win,width=400,height=300,bg='#0000aa')

f.place(x=0,y=0)

c=tk.Canvas(f,bd=2,width=200,height=200)

c.place(x=0,y=0)

c.create_rectangle(10,10,50,50,width=4,tags='r1')

def p(event):
    print('tag_bind   ok')

c.tag_bind('r1','<1>',p)

coord = 10, 50, 240, 210
arc = c.create_arc(coord, start=0, extent=150, fill="blue")

c.pack()

img=tk.PhotoImage(file='image/background.png')

c.create_image(20,20,40,40,image=img)



'''
def remove(event,l):
    l.grid_forget()
    #l.config(width=5,height=6)
    
grid=tk.Label(f,text='123',wraplength=1)

l2=tk.Label(f,text='abc')
l2.grid(row=1,column=2)

grid.bind('<1>',lambda x:remove(x,grid))
grid.grid(row=1,column=1)
'''

win.mainloop()

