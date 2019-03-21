import tkinter as tk
from tkinter import font
import csv
import codecs

def sortAccord(array,copy):
    l = [i.split() for i in array.get(0,6)]
    array.delete(0,6)
    print("\nThis is it\n")
    print(l,array)
    l2 = {}
    for i in l:
        l2[i[copy].lower()] = i
        #print(i,new_i)
    #print(l2)
    
    l4 = list(sorted(l2.keys()))
    for i in l4:
        array.insert(tk.END,"{:<20s}{:<20s}{:<20s}{:<20s}".format(l2[i][0],l2[i][1],l2[i][2],l2[i][3]))
    
win = tk.Tk()
#win.geometry("400x200")
my_font = font.Font(family="Monaco", size=12)
l1 = tk.Listbox(win,width=100,font = my_font)

data = []
with open("eventListNew.csv",encoding="utf-8-sig") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        data.append([row[0],row[1],row[2],row[3]])
csvFile.close()
#data = ["hello how are you".split(),"i am not fine".split(),"what about you man?".split(),"I'm fine bro, Chill!".split()]

for i in data:
    l1.insert(tk.END,"{:<20s}{:<20s}{:<20s}{:<20s}".format(i[0],i[1],i[2],i[3]))

#v = tk.StringVar()

buttonFrame = tk.Frame()
but1 = tk.Button(buttonFrame,text=" Name ",command = lambda: sortAccord(l1,0))
but2 = tk.Button(buttonFrame,text=" Room Type ",command = lambda: sortAccord(l1,1))
but3 = tk.Button(buttonFrame,text=" Date ",command = lambda: sortAccord(l1,2))
but4 = tk.Button(buttonFrame,text=" Venue ",command = lambda: sortAccord(l1,3))
but1.pack(side=tk.LEFT,padx=10,pady=10)
but2.pack(side=tk.LEFT,padx=15,pady=10)
but3.pack(side=tk.LEFT,padx=35,pady=10)
but4.pack(side=tk.LEFT,padx=20,pady=10)
buttonFrame.pack(side=tk.TOP)

#e = tk.Entry(win,textvariable = v)
#e.pack()
l1.pack()
win.mainloop()
