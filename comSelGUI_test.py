''' 利用tkinter 和 serial两个模块的功能，实现几个简单的COM口选择，打开/关闭端口，跳出对话框提示打开是否成功'''

import tkinter as tk
from  tkinter  import ttk
import serial


#部署整体界面
com_sel = tk.Tk()
com_sel.title("pySerialPort || Author Jingyan Chen All Right Reserve")
com_sel.geometry("400x100")

#

#部署串口设备
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM10'
#end 部署串口设备



#部署COM选择页面

#端口被选中的事件
def com_sel_handle(*args):   
    print(comboxList.get()) 

com_value = tk.StringVar()
comboxList = ttk.Combobox(com_sel,textvariable=com_value,state="normal")
comboxList["values"] = ("COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10","COM11","COM12","COM13","COM14","COM15","COM16","COM17","COM18","COM19","COM20")
comboxList.current(0)
comboxList.bind("<<ComboboxSelected>>",com_sel_handle)
comboxList.place(x=100,y=20)
#end 部署COM选择页面

#部署label
tk.Label(com_sel, text='COM SEL:', font=('Arial', 10)).place(x=10, y=20)
sys_status_var =  tk.StringVar()
sys_status_var.set('INITIAL SUCCESS..')
l = tk.Label(com_sel,textvariable=sys_status_var ,font=('Arial', 10))
l.place(x=10, y=70)
#end部署label

#部署确定按键


button_var =  tk.StringVar()
button_var.set("Open")


on_hit = False
def com_sel_ok_button_handle():
    global on_hit
    if on_hit == False:
        ser.port = comboxList.get()
        try:
            ser.open()
            if ser.is_open:
                on_hit = True
                print("open_com success")
                sys_status_var.set("Open "+ ser.port +" Success")
                button_var.set("Close")
            else:
                on_hit = False
                print("open_com failed")       
                sys_status_var.set("Open "+ ser.port +" Failed")         
        except:
           print("open_com failed")
           sys_status_var.set("Open "+ ser.port +" Failed")

        
    else:
        on_hit = False
        ser.close()
        print("close com success")
        sys_status_var.set("Close "+ ser.port +" Success")  
        button_var.set("Open")
        comboxList.state = 'normal' 
        


ok_button = tk.Button(com_sel,textvariable=button_var,font=('Arial',10),width=10,height=1,command=com_sel_ok_button_handle)
ok_button.place(x=300,y=16)


def open_gui_handle():
    '''打开一个专业的全黑屏的串口收发界面，实现类似SERURT的功能，能实现记录报文等功能'''
    if on_hit == True:
        pass
        #打开新的类似SCEURT CRT的收发界面
    else:
        print("open gui failed")
        sys_status_var.set("Open "+ "GUI" +" Failed port not open")

open_gui_button = tk.Button(com_sel,text="Start GUI",font=('Arial',10),width=10,height=1,command=open_gui_handle)
open_gui_button.place(x=300,y=65)

#end 部署确定按键


com_sel.mainloop()
