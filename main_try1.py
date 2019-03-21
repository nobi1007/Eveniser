from tkinter import *
#from events  import *
from tkinter import font
import csv
import codecs


def whichSelected () :
    print("At %s of %d" % (select.curselection(), len(data)))
    return int(select.curselection()[0])

def addEntry () :
    na,rm,dt,ven = [nameVar.get(), rmtypeVar.get(), dateVar.get(), venueVar.get()]
    for i in data:
        print(i)
        if dt in i and rm in i:
            messageBox.delete('1.0',END)
            messageBox.insert(END,"This event can not be registered. Either because of slot and venue might be clashing")
            messageBox.tag_add("start", "1.0", "1.100")
            messageBox.tag_config("start", background="white", foreground="red")
            break
    else:
        data.append ([nameVar.get(), rmtypeVar.get(), dateVar.get(), venueVar.get()])
        messageBox.delete('1.0',END)
        messageBox.insert(END,"Your event "+nameVar.get()+" was successfully registered")
        messageBox.tag_add("start", "1.0", "1.100")
        messageBox.tag_config("start", background="white", foreground="green")
    setSelect ()

def updateEntry() :
    data[whichSelected()] = [nameVar.get(), rmtypeVar.get(), dateVar.get(), venueVar.get()]
    setSelect ()

def deleteEntry() :
    try:
        del data[whichSelected()]
    except: IndexError
    setSelect ()

def loadEntry  () :
    name, rmtype, date, venue  = data[whichSelected()]
    nameVar.set(name)
    rmtypeVar.set(rmtype)
    dateVar.set(date)
    venueVar.set(venue)

def makeWindow () :
    global nameVar, rmtypeVar, dateVar, venueVar, select, data, messageBox
    data=[]

    win = Tk()
    
    my_font = font.Font(family="Monaco", size=12)
    select = Listbox(win,width=100,font = my_font)

    with open("eventListNew.csv",encoding="utf-8-sig") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            data.append([row[0],row[1],row[2],row[3]])
    csvFile.close()

    for i in data:
        select.insert(END,"{:<20s}{:<20s}{:<20s}{:<20s}".format(i[0],i[1],i[2],i[3]))


    buttonFrame = Frame()
    but1 = Button(buttonFrame,text=" Name ",command = lambda: sortAccord(0))
    but2 = Button(buttonFrame,text=" Room Type ",command = lambda: sortAccord(1))
    but3 = Button(buttonFrame,text=" Date ",command = lambda: sortAccord(2))
    but4 = Button(buttonFrame,text=" Venue ",command = lambda: sortAccord(3))
    but1.pack(side=LEFT,padx=10,pady=10)
    but2.pack(side=LEFT,padx=15,pady=10)
    but3.pack(side=LEFT,padx=35,pady=10)
    but4.pack(side=LEFT,padx=20,pady=10)
    buttonFrame.pack(side=TOP)

    #e = tk.Entry(win,textvariable = v)
    #e.pack()
    select.pack()


    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Event Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Room Type").grid(row=1, column=0, sticky=W)
    rmtypeVar= StringVar()
    rmtype= Entry(frame1, textvariable=rmtypeVar)
    rmtype.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Date").grid(row=2, column=0, sticky=W)
    dateVar = StringVar()
    date = Entry(frame1, textvariable=dateVar)
    date.grid(row=2, column=1, sticky=W)
    
    Label(frame1, text="Venue").grid(row=3, column=0, sticky=W)
    venueVar = StringVar()
    venue = Entry(frame1, textvariable=venueVar)
    venue.grid(row=3, column=1, sticky=W)
    
    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b1.pack(side=LEFT,padx=10,pady=20); b2.pack(side=LEFT,padx=10,pady=20)
    b3.pack(side=LEFT,padx=10,pady=20); b4.pack(side=LEFT,padx=10,pady=20)


    #frame3 = Frame(win)       # select of names
    #frame3.pack()
    #scroll = Scrollbar(frame3, orient=VERTICAL)
    #select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    #scroll.config (command=select.yview)
    #scroll.pack(side=RIGHT, fill=Y)
    #select.pack(side=LEFT,  fill=BOTH, expand=1)


    frame4 = Frame(win)     #message box label
    frame4.pack()

    messageLabel = Label(frame4,text="Message Box")
    messageLabel.pack(padx=10,pady=10)
    messageBox = Text(frame4,height=3,width=50)
    messageBox.insert(END,"j")
    messageBox.pack(side = LEFT,padx=10,pady=10)
    return win

def sortAccord(copy):
    global l2
    l = [i.split() for i in select.get(0,END)]
    select.delete(0,END)
    #print("\nThis is it\n")
    #print(l,array)
    l2 = {}
    for i in l:
        x = i[copy].lower()
        if x not in l2.keys():
            l2[x] = [i]
        else:
            l2[x] += [i]

    l4 = list(sorted(l2.keys()))
    for i in l4:
        for j in range(len(l2[i])):
            select.insert(END,"{:<20s}{:<20s}{:<20s}{:<20s}".format(l2[i][j][0],l2[i][j][1],l2[i][j][2],l2[i][j][3]))

def setSelect() :
    data.sort()
    select.delete(0,END)
    for i in data:
        select.insert(END,"{:<20s}{:<20s}{:<20s}{:<20s}".format(i[0],i[1],i[2],i[3]))

    #print(l2)

#win.geometry("400x200")
win = makeWindow()
setSelect ()
win.mainloop()
