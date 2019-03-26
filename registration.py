from tkinter import *
from tkinter import messagebox as msg
import csv


database = {}

with open('people.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
#print(lines)
for i in range(len(lines)):
    if lines[i]!=[]:
        database[lines[i][0]] = lines[i][1]
    
#database = {"hem":"qwerty","admin":"admin"}

def checkId(a):
    global database
    if a in database.keys():
        msg.showerror("Failed!","User id not available")
    else:
        msg.showinfo("Success","User id is available")

def checkPass(a,ra):
    global database
    if a != ra:
        msg.showerror("Failed!","Password does not match")
    else:
        msg.showinfo("Success","Password Matched")

def checkRegister(a,b,c,rb):
    global database,lines,win
    if c=="" or a=="" or b=="":
        msg.showerror("Failed!","Invalid Input")
    elif a in database.keys():
        msg.showerror("Failed!","User id not available")
    elif b != rb:
        msg.showerror("Failed!","Password does not match")
    else:
        msg.showinfo("Success!","Registered Successfully")
        lines.append([a,b,c])
        with open('people.csv', 'w',newline = "") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        writeFile.close()
        win.destroy()
        
win = Tk()
win.title("Registration")
win.geometry("400x200+400+100")
win.resizable(0,0)

f1 = Frame()
f1.pack()
Label(f1,text="Name: ").grid(row=0,column=0)    #name field
nameVar = StringVar()
Entry(f1,textvariable = nameVar).grid(row=0,column=1) 

Label(f1,text="User Id: ").grid(row=1,column=0)    #userid field
idVar = StringVar()
Entry(f1,textvariable = idVar).grid(row=1,column=1)
Label(f1,text="       ").grid(row=1,column=2)
Label(f1,text="       ").grid(row=1,column=4)
Button(f1,text = "Check",command = lambda: checkId(idVar.get().strip())).grid(row=1,column=3)

Label(f1,text = "Enter Password: ").grid(row=2,column=0)
passVar = StringVar()
Entry(f1,textvariable = passVar,show="*").grid(row=2,column=1)

Label(f1,text = "Re-enter Password: ").grid(row=3,column=0)
repassVar = StringVar()
Entry(f1,textvariable = repassVar,show="*").grid(row=3,column=1)
Label(f1,text="       ").grid(row=3,column=2)
Label(f1,text="       ").grid(row=3,column=4)
Button(f1,text = "Check",command = lambda: checkPass(passVar.get().strip(),repassVar.get().strip())).grid(row=3,column=3)

f2 = Frame()
f2.pack()
b1 = Button(f2,text="Register",width = "20",command = lambda: checkRegister(idVar.get().strip(),passVar.get().strip(),nameVar.get().strip(),repassVar.get().strip()))

#b1.config(state="disabled")
b1.grid(row=4,column=1)

readFile.close()
win.mainloop()




