''' 利用tkinter 和 serial两个模块的功能，实现几个简单的COM口选择，打开/关闭端口，跳出对话框提示打开是否成功'''

import tkinter as tk
from  tkinter  import ttk
import serial
import serial.tools.list_ports
import os
import threading
from time import sleep
import datetime
import oscilloscope

#部署整体界面
com_sel = tk.Tk()
com_sel.title("pySerialPort || Author Jingyan Chen All Right Reserve")
com_sel.geometry("400x100")

#

#部署串口设备

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM10'
ser.timeout = 3600

''' 串口收到数据的服务函数
    接收到的数据，再前端加入时间数据
'''
def rcv_data():
    
    while True:
        rcv=ser.read()
        rcv=rcv.decode() 
        print(rcv,end='')
        

'''控制台发送数据的服务函数'''
def send_data():
    while True:
        #nowTime=datetime.datetime.now().strftime('%H:%M:%S comegene command:')
        send_data=input()
        send_data = send_data + '\r\n'
        if("21" in send_data or "open_temp_gui" in send_data):
            #ser.close()
            #st = comboxList.get()
            #ser.port = st.split(" ",1)[0]
            #oscilloscope.set_com_str(ser.port)
            #oscilloscope.osc_run()
            print("open osc moudle\r\n")

        ser.write(send_data.encode())
#end 部署串口设备



#部署COM选择页面

#端口被选中的事件
def com_sel_handle(*args):   
    print(comboxList.get()) 

com_value = tk.StringVar()
comboxList = ttk.Combobox(com_sel,textvariable=com_value,state="normal")
port_list = list(serial.tools.list_ports.comports()) #获得可用的端口list
comboxList["values"] = port_list
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
        st = comboxList.get()
        #print(type(st))
        #print(st.split(" ",1)[0])
        ser.port = st.split(" ",1)[0]
        try:
            ser.open()
            if ser.is_open:
                on_hit = True
                print("open_com success")
                sys_status_var.set("Open "+ ser.port +" Success")
                button_var.set("Close")

                #部署接收数据线程
                th=threading.Thread(target=rcv_data)
                th.setDaemon(True)
                th.start()

                #部署发送数据线程
                th2=threading.Thread(target=send_data)
                th2.setDaemon(True)
                th2.start()      

                com_sel.iconify()
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
        com_sel.iconify()
        #打开新的类似SCEURT CRT的收发界面
    else:
        print("open gui failed")
        sys_status_var.set("Open "+ "GUI" +" Failed port not open")

open_gui_button = tk.Button(com_sel,text="Start GUI",font=('Arial',10),width=10,height=1,command=open_gui_handle)
open_gui_button.place(x=300,y=65)

#end 部署确定按键





com_sel.mainloop()
