from tkinter import *
from tkinter import messagebox
import subprocess as sb
import csv

database = {}

with open('people.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
#print(lines)
for i in range(len(lines)):
    if lines[i]!=[]:
        database[lines[i][0]] = lines[i][1]
def goBack():
    global win
    win.destroy()
    sb.call("main_test1.py",shell=True)

def check(a,b):
    global database,win
    
    if not a in database.keys():
        messagebox.showerror("Failed!","User not registered")
        return
    elif database[a] == b:
        messagebox.showinfo("Congrats","Login Successful")
        win.destroy()
        sb.call("mix_try1.py",shell=True)
    else:
        messagebox.showwarning("Failed!","Invalid Password")

win = Tk()
win.title("Login Page")
win.geometry("300x150+500+200")
win.resizable(0,0)

f1 = Frame()
f1.pack()
Label(f1,text="User Id: ").grid(row=0,column=0,pady=4,padx=10)
idVar = StringVar()
Entry(f1,textvariable = idVar).grid(row=0,column=1)
Label(f1,text="Password: ").grid(row=1,column=0,pady=4,padx=10)
passVar = StringVar()
Entry(f1,show = "*",textvariable = passVar).grid(row=1,column=1)
f2 = Frame()
f2.pack()
Button(f2,text="Submit",width="12",command = lambda:check(idVar.get().strip(),passVar.get().strip())).grid(row=2,column=0,pady=4,padx=10)
Button(f2,text="Back",width="12",command = goBack).grid(row=2,column=1,pady=4,padx=10)
readFile.close()
win.mainloop()
