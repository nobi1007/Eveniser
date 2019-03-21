from tkinter import *
from events  import *

def whichSelected () :
    print("At %s of %d" % (select.curselection(), len(eventlist)))
    return int(select.curselection()[0])

def addEntry () :
    eventlist.append ([nameVar.get(), eventVar.get(), dateVar.get(), venueVar.get()])
    setSelect ()

def updateEntry() :
    eventlist[whichSelected()] = [nameVar.get(), eventVar.get(), dateVar.get(), venueVar.get()]
    setSelect ()

def deleteEntry() :
    del eventlist[whichSelected()]
    setSelect ()

def loadEntry  () :
    name, event, date, venue  = eventlist[whichSelected()]
    nameVar.set(name)
    eventVar.set(event)
    dateVar.set(date)
    venueVar.set(venue)

def makeWindow () :
    global nameVar, eventVar, dateVar, venueVar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Event Type").grid(row=1, column=0, sticky=W)
    eventVar= StringVar()
    event= Entry(frame1, textvariable=eventVar)
    event.grid(row=1, column=1, sticky=W)

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

    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    return win

def setSelect () :
    eventlist.sort()
    select.delete(0,END)
    for name,event, date,venue  in eventlist :
        select.insert (END, name)

win = makeWindow()
setSelect ()
win.mainloop()
