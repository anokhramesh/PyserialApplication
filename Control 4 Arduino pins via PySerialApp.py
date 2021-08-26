#ON/OFF Button with Change Image and Text
from tkinter import *
import serial
arduinoData = serial.Serial('com11', 9600)
root=Tk()
root.geometry('500x600')
root.title("Pyserial App")
root.iconbitmap("python_logo_icon.ico")
Appname=Label(root,text='WELCOME TO ANOKHAUTOMATION',fg='purple',bg='white',font="Georgea 20 bold")
Appname.pack(pady=10)
root.configure(background="yellow")
on_image =PhotoImage(file='Toggle-off-96.png')
off_image =PhotoImage(file='Toggle-on-96.png')
global on1
global on2
global on3
global on4
on1 =True
on2 =True
on3 =True
on4 =True
#Define Button1 function
def Button_1():
    global on1
    if on1:
        arduinoData.write(b'a')  # send charactor 'a' when button1 pressed
        button_1.config(image=off_image)
        load1_label.config(text="LOAD 1 is Off",fg="blue")
        on1=False
    else:
        arduinoData.write(b'b')  # send charactor 'b' when button2pressed
        button_1.config(image=on_image)
        load1_label.config(text="LOAD 1 is ON",fg="red")
        on1=True
#Define button2 function
def Button_2():
        global on2
        if on2:
            arduinoData.write(b'c')  # send charactor 'c' when button1 pressed
            button_2.config(image=off_image)
            load2_label.config(text="LOAD 2 is Off", fg="blue")
            on2 = False
        else:
            arduinoData.write(b'd')  # send charactor 'd' when button2pressed
            button_2.config(image=on_image)
            load2_label.config(text="LOAD 2 is ON", fg="red")
            on2 = True
#Function for Button-3
def Button_3():
    global on3
    if on3:
        arduinoData.write(b'e')  # send charactor 'e' when button1 pressed
        button_3.config(image=off_image)
        load3_label.config(text="LOAD 3 is Off",fg="blue")
        on3=False
    else:
        arduinoData.write(b'f')  # send charactor 'f' when button2pressed
        button_3.config(image=on_image)
        load3_label.config(text="LOAD 3 is ON",fg="red")
        on3=True
#Define button2 function
def Button_4():
        global on4
        if on4:
            arduinoData.write(b'g')  # send charactor 'g' when button1 pressed
            button_4.config(image=off_image)
            load4_label.config(text="LOAD 4 is Off", fg="blue")
            on4 = False
        else:
            arduinoData.write(b'h')  # send charactor 'h' when button2pressed
            button_4.config(image=on_image)
            load4_label.config(text="LOAD 4 is ON", fg="red")
            on4 = True
#label for Load-1
load1_label=Label(root,text="LOAD 1 is OFF",bg="yellow",fg="blue",font=("Verdana",15,"bold"))
load1_label.pack(pady=1,)
#button for Load-1
button_1=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_1)
button_1.pack(pady=1)
#label for Load-2
load2_label=Label(root,text="LOAD 2 is OFF",bg="yellow",fg="blue",font=("Verdana",15,"bold"))
load2_label.pack(pady=1)
#button for Load-2
button_2=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_2)
button_2.pack(pady=1)
#label for Load-3
load3_label=Label(root,text="LOAD 3 is OFF",bg="yellow",fg="blue",font=("Verdana",15,"bold"))
load3_label.pack(pady=1)
#button for Load-3
button_3=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_3)
button_3.pack(pady=1)
#label for Load-4
load4_label=Label(root,text="LOAD 4 is OFF",bg="yellow",fg="blue",font=("Verdana",15,"bold"))
load4_label.pack(pady=1)
#button for Load-4
button_4=Button(root,image=off_image,bg='yellow',borderwidth=0,command=Button_4)
button_4.pack(pady=1)
root.mainloop()