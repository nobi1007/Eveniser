from tkinter import *
from tkinter import font
import csv
import codecs
import subprocess as sb

def whichSelected () :
    #print("At %s of %d" % (select.curselection(), len(data)))
    return int(select.curselection()[0])

def addEntry () :
    na,rm,dt,ven,rat = [nameVar.get(), rmtypeVar.get(), dateVar.get(), venueVar.get(), ratingVar.get()]
    for i in data:
        #print(i)
        if dt in i and rm in i:
            messageBox.delete('1.0',END)
            messageBox.insert(END,"This event can not be registered. Either because of slot and venue might be clashing")
            messageBox.tag_add("start", "1.0", "1.100")
            messageBox.tag_config("start", background="white", foreground="red")
            break
    else:
        data.append ([nameVar.get(), rmtypeVar.get(), dateVar.get(), venueVar.get(),ratingVar.get()])
        messageBox.delete('1.0',END)
        messageBox.insert(END,"Your event "+nameVar.get()+" was successfully registered")
        messageBox.tag_add("start", "1.0", "1.100")
        messageBox.tag_config("start", background="white", foreground="green")
    setSelect ()

def updateEntry() :
    try:
        messageBox.delete('1.0',END)
        messageBox.insert(END,"Your event "+nameVar.get()+" was updated")
        messageBox.tag_add("start", "1.0", "1.100")
        messageBox.tag_config("start", background="white", foreground="grey")
        data[whichSelected()] = [nameVar.get(), rmtypeVar.get(), dateVar.get(), venueVar.get(), ratingVar.get()]
    except: IndexError
    setSelect ()
def deleteEntry() :
    try:
        messageBox.delete('1.0',END)
        messageBox.insert(END,"Your event "+data[whichSelected()][0]+" at "+data[whichSelected()][3]+" was successfully deleted")
        messageBox.tag_add("start", "1.0", "1.100")
        messageBox.tag_config("start", background="white", foreground="blue")
        del data[whichSelected()]
    except: IndexError
    setSelect ()

def loadEntry() :
    name, rmtype, date, venue, rating  = data[whichSelected()]
    nameVar.set(name)
    rmtypeVar.set(rmtype)
    dateVar.set(date)
    venueVar.set(venue)
    ratingVar.set(rating)

def back():
    win.destroy()
    sb.call("main_test1.py",shell=True)

def makeWindow () :
    global nameVar, rmtypeVar, dateVar, venueVar, ratingVar, select, data, messageBox,win
    data=[]

    win = Tk()
    Button(win,text=" BACK ",command=back).pack(side=LEFT)
    f0 = Frame()
    f0.pack()
    Label(f0,text="~ Sort the events ~",font=("Bookman Old Style",20)).pack(side=TOP,pady=10)
    f1 = Frame()
    scroll = Scrollbar(f1)
    scroll.pack(side=RIGHT,fill=Y)
    my_font = font.Font(family="Monaco", size=12)
    select = Listbox(f1,width=90,font = my_font,yscrollcommand = scroll.set)


    with open("eventListNew.csv",encoding="utf-8-sig") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            data.append([row[0],row[1],row[2],row[3],row[4]])
    csvFile.close()

    for i in data:
        select.insert(END,"{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}".format(i[0],i[1],i[2],i[3],i[4]))


    buttonFrame = Frame()
    but1 = Button(buttonFrame,text=" Name ",command = lambda: sortAccord(0))
    but2 = Button(buttonFrame,text=" Room Type ",command = lambda: sortAccord(1))
    but3 = Button(buttonFrame,text=" Date ",command = lambda: sortAccord(2))
    but4 = Button(buttonFrame,text=" Venue ",command = lambda: sortAccord(3))
    but5 = Button(buttonFrame,text=" Ratings ",command = lambda: sortAccord(4))
    

    but1.grid(row=0,column=0)
    Label(buttonFrame,text=" "*40).grid(row=0,column=1)
    but2.grid(row=0,column=2)
    Label(buttonFrame,text=" "*40).grid(row=0,column=3)
    but3.grid(row=0,column=4)
    Label(buttonFrame,text=" "*40).grid(row=0,column=5)
    but4.grid(row=0,column=6)
    Label(buttonFrame,text=" "*40).grid(row=0,column=7)
    but5.grid(row=0,column=8)
    buttonFrame.pack(side=TOP)
    select.pack(side = LEFT, fill = BOTH,pady = 10)
    scroll.config( command = select.yview )
    f1.pack()

    fLine = Frame(win)
    fLine.pack()

    canvasLine = Canvas(height=1,width=60)
    canvasLine.pack(fill=BOTH,expand=1)
    canvasLine.create_line(100,20,700,20)

    downFrame = Frame(win)
    downFrame.pack(side=BOTTOM)
    frame12 = Frame(downFrame)
    frame12.pack(side=LEFT,padx=80)
    frame12Head = Frame(frame12)
    frame12Head.grid(row=0,column=0)
    Label(frame12Head,text="- Add & Update -",font=("Bookman Old Style",15)).pack(pady=10)

    frame1 = Frame(frame12)
    frame1.grid(row=1,column=0)

    Label(frame1, text="Event Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W,pady=10)

    Label(frame1, text="Room Type").grid(row=1, column=0, sticky=W)
    rmtypeVar= StringVar()
    rmtype= Entry(frame1, textvariable=rmtypeVar)
    rmtype.grid(row=1, column=1, sticky=W,pady=10)

    Label(frame1, text="Date").grid(row=2, column=0, sticky=W)
    dateVar = StringVar()
    date = Entry(frame1, textvariable=dateVar)
    date.grid(row=2, column=1, sticky=W,pady=10)
    
    Label(frame1, text="Venue").grid(row=3, column=0, sticky=W)
    venueVar = StringVar()
    venue = Entry(frame1, textvariable=venueVar)
    venue.grid(row=3, column=1, sticky=W,pady=10)

    Label(frame1, text="Rating").grid(row=4, column=0, sticky=W)
    ratingVar = StringVar()
    options = list("54321")
    ratingVar.set('5')
    dropdown = OptionMenu(frame1,ratingVar,*options)
    dropdown.grid(row=4, column=1, sticky=W,pady=10)
    
    frame2 = Frame(frame12)       # Row of buttons
    frame2.grid(row=2,column=0)
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b1.pack(side=LEFT,padx=10,pady=20); b2.pack(side=LEFT,padx=10,pady=20)
    b3.pack(side=LEFT,padx=10,pady=20); b4.pack(side=LEFT,padx=10,pady=20)

    fLine2 = Frame(downFrame)
    fLine2.pack(side=LEFT)

    canvasLine2 = Canvas(fLine2,height=10,width=2)
    canvasLine2.pack(fill=BOTH,expand=1)
    canvasLine2.create_line(150,0,150,300)


    frame4 = Frame(downFrame)     #message box label
    frame4.pack(side=LEFT,padx=80)
    
    messageLabel = Label(frame4,text="! Message Box !",font=("Bookman Old Style",15))
    messageLabel.pack(padx=10,pady=10)
    messageBox = Text(frame4,height=10,width=30)
    #messageBox.insert(END,"j")
    messageBox.pack(side = LEFT,padx=10,pady=10)
    return win

def sortAccord(copy):
    global l2
    l = [i.split() for i in select.get(0,END)]
    select.delete(0,END)
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
            select.insert(END,"{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}".format(l2[i][j][0],l2[i][j][1],l2[i][j][2],l2[i][j][3],l2[i][j][4]))

def setSelect() :
    data.sort()
    select.delete(0,END)
    for i in data:
        select.insert(END,"{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}".format(i[0],i[1],i[2],i[3],i[4]))

#win.geometry("400x200")
wind = makeWindow()
wind.title(" Eveniser ")
wind.geometry("1000x700+160+20")
wind.resizable(0,0)
setSelect ()
win.mainloop()
