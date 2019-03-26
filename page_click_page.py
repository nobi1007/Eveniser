from tkinter import *

def new():
    inside = Tk()
    inside.mainloop()

main = Tk()

frame1 = Frame(main)
frame1.pack()

Button(master = frame1,text = "Hit me!", command = new).pack()

main.mainloop()
