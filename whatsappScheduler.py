import pywhatkit
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def reset():
    pass   

def send():
    num=no.get()
    msg=message.get()
    H=Hours.get()
    try:
        H=int(H)
    except:
        messagebox.showerror('error','Select time')
    print(H)
    M= Minutes.get()
    try:
        M=int(M)
    except:
        messagebox.showerror('error','Select time')
    print(M)
    messagebox.showinfo('info','Click Okay')
    pywhatkit.sendwhatmsg('%s'%num,'%s'%msg,H,M,50)
    messagebox.showinfo('info','Successfully sent')
    

global no
global message
global H
global M

screen = Tk()
screen.geometry("400x400")
Label(text="Enter Number (eg: 771236547 )", fg="black",font=("calibri",13)).place(x=10,y=10)
no = StringVar()
Entry(textvariable=no,width=19,bd=0,font=("arial",25)).place(x=10,y=40)

Label(text="Enter Message ( eg : Hello )", fg="black",font=("calibri",13)).place(x=10,y=90)
message= StringVar()
Entry(textvariable=message,width=19,bd=0,font=("arial",25)).place(x=10,y=120)

Label(text="Select Time ", fg="black",font=("calibri",13)).place(x=10,y=160)
Hours= Combobox(screen,values=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','00'],font="Roboto 10",width=17,state="r")
Hours.place(x=10,y=200)
Hours.set("Hour")

Minutes= Combobox(screen,values=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60'],font="Roboto 10",width=17,state="r")
Minutes.place(x=250,y=200)
Minutes.set("Minutes")



Button(text="Send",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=send).place(x=100,y=300)
#Button(text="Send",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=reset).place(x=100,y=350)
screen.mainloop()

