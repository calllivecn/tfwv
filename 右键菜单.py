from tkinter import *
root = Tk()
menubar = Menu(root,tearoff=0)

def printItem():
    print('popup menu')

filemenu = Menu(menubar,tearoff = 0)
for k in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    filemenu.add_command(label = k,command = printItem)
#filemenu.add_separator()
menubar.add_cascade(label = 'Language',menu = filemenu)
#此时就不要将root的menu设置为menubar了
#root['menu'] = menubar
def popup(event):
    #显示菜单
    menubar.post(event.x_root,event.y_root)

def close(event):
    print('<Leave>')
    menubar.unpost()

#在这里相应鼠标的右键事件，右击时调用popup,此时与菜单绑定的是root，可以设置为其它的控件，在绑定的控件上右击就可以弹出菜单
menubar.bind('<Leave>',close)
root.bind('<Button-3>',popup)
root.mainloop()
