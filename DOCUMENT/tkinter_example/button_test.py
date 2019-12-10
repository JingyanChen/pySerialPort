#create main windows and use button widget
import tkinter as tk

windows = tk.Tk()
windows.title("my windows")
windows.geometry('500x300')

var = tk.StringVar() # 创建一个由tk类静态定义的类型stringVar对象，为后期按键修改字符串做准备
l = tk.Label(windows,textvariable=var , bg='green',fg='white',font=('Arial', 12),width=30 ,height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")
    
b = tk.Button(windows,text='hit me',font=('Arial',12),width=10,height=1,command=hit_me)
b.pack()

windows.mainloop()