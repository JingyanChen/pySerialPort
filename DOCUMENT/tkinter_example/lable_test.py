#create main windows and use label widget

import tkinter as tk  #导入tk模块

#1 实例化windows界面
window = tk.Tk()

#2 给窗口取名字
window.title('My Windows')

#3 设定窗口的大小
window.geometry('500x300')

#4 利用类的静态方法生成标签模块
lable = tk.Label(window,text = "This is my first Tkinter",bg='green',font=('Arial',12),width=30,height=2)

#5 放置标签模块到window
lable.pack()

#6 主循环显示，不断刷新
window.mainloop()


