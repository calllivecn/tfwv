#!/usr/bin/env python3
#coding=utf-8

import copy

import tkinter as tk

from tkinter import ttk


win=tk.Tk(className='(-_-!)')

win.minsize(800,600)

f1=tk.Frame(win,bg='#afaf12')
f2=tk.Frame(win,bg='#ff00ff')

f1.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)
f2.place(relx=0,rely=0.7,relwidth=0.7,relheight=0.3)

f3=tk.Frame(win,bg='#123456')
f3.place(relx=0,rely=0,relwidth=0.7,relheight=0.7)

f3_f1=tk.Frame(f3,bg='#999999')
f3_f1.place(relx=0,rely=0,relwidth=1,relheight=0.1)

f3_f2=tk.Frame(f3,bg='#888888')
f3_f2.place(relx=0,rely=0.1,relwidth=0.1,relheight=0.9)

f3_f3=tk.Frame(f3,bg='#aaaaaa')
f3_f3.place(relx=0.9,rely=0.1,relwidth=0.1,relheight=0.9)

f3_f4=tk.Label(f3,bg='#123123')
f3_f4.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.9)

f2_f1=tk.Frame(f2,bg='#998736')
f2_f1.place(relx=0,rely=0,relwidth=1,relheight=0.2)#(side='bottom',)

f2_f2=tk.Frame(f2,bg='#627458')

f2_f2.rowconfigure(9)
f2_f2.columnconfigure(17)
f2_f2.place(relx=0,rely=0.2,relwidth=1,relheight=0.8)

class P():
    P=None
    width=None
    height=None
    def move(self,event):
        self.P.config(bg='#999999')
        
    def remove(self,event):
        self.P.config(bg='#ffffff')

    def __init__(self,frame,char,type_,color):
        if char=='10':
            self.P=tk.Label(frame,text='{}{}'.format(char,type_),foreground=color,bg='#ffffff',anchor='nw',
                        width=2,height=7,wraplength=15)
        else:
            self.P=tk.Label(frame,text='{}{}'.format(char,type_),foreground=color,bg='#ffffff',anchor='nw',
                        width=2,height=7,wraplength=1)
        self.P.bind('<Enter>',self.move)
        self.P.bind('<Leave>',self.remove)
        self.width=self.P.winfo_width()
        self.height=self.P.winfo_height()
            
class Pk():
    P={}
    
    Y=True
    def hkfb(self,event):
        if self.Y:
            self.P.config(height=9)
            self.Y=False
        else:
            self.P.config(height=7)
            self.Y=True
        

        
    def __init__(self,frame):
        index=0
        for type_,color in [('方','#ff0000'),('梅','#000000'),('红','#ff0000'),('黑','#000000')]:
            for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                self.P[index]=P(frame,j,type_,color)
                index+=1
        
        self.P[index]=P(frame,'JOKER','','#000000')
        index+=1
        self.P[index]=P(frame,'JOKER','','#ff0000')
        index+=1
        self.P[index]=P(frame,'配牌','','#aaaaaa')
        
        
    def get(self,index):
        return self.P[index]



def temp1(y,label):
    print(y,label['bg'])

def thgf(w=None,h=None):
    
    for i in range(54):
        pk.get(i).P.pack(side='left',anchor='nw')

pk=Pk(f2_f2)

thgf()

win.mainloop()
