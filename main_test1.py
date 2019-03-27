from tkinter import *
from tkinter import messagebox as msg
from tkinter import font
import subprocess as sb

def callLogin():
    global win
    win.destroy()
    sb.call("login.py",shell=True)    
    

def callRegister():
    global win
    #win.destroy()
    sb.call("registration.py",shell=True)    

def callGuest():
    global win
    win.destroy()
    sb.call("guestPage.py",shell=True)    

win = Tk()
win.title("Eveniser - Login")
win.geometry("500x300+400+100")
win.resizable(0,0)
f1 = Frame()
f1.pack()
Label(f1,text="Eveniser",font=("Bookman Old Style", 30)).grid(row=0,column=1)

f2 = Frame()
f2.pack()
Label(f2,text="\n\n\n").grid(row=1,column=1)
b1 = Button(f2,text = "Login", width="12",command = callLogin)
b1.grid(row=2,column=0)
Label(f2,text="                  ").grid(row=2,column=1)
b2 = Button(f2,text = "Register", width="12",command = callRegister)
b2.grid(row=2,column=2)

f3 = Frame()
f3.pack()
Label(f3,text="\n").grid(row=3,column=1)
b3 = Button(f3,text = "Guest", width="15",command = callGuest)
b3.grid(row=4,column=1)
 
win.mainloop()

