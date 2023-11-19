from tkinter import *


def addnewTeam(event):
    """_summary_
        our adding part that we can use it to add new team to the databas
    Args:
        event (_type_): _description_
    """
    def addToDatabase(event):
        """_summary_
            get info of the team and add it to the database
        Args:
            event (_type_): _description_
        """
        print('add')
    addNewRoot = Tk()
    # title of the adding part
    addNewRoot.title('add new team')
    # icon of the adding part
    addNewRoot.iconbitmap('icons//addNewOne.ico')
    addNewRoot.configure(bg='#EAD7BB')
    # geometry of the adding part
    addNewRoot.geometry('%dx%d+%d+%d'%(300,300,1100,300))
    
    # name adding part
    nameFram = Frame(master=addNewRoot, width=500, height=20, bg='#EAD7BB')
    nameFram.pack_propagate(False)
    nameFram.pack()
    nameLabel = Label(master=nameFram, text='team name: ', bg = '#EAD7BB')
    nameLabel.pack(side='left')
    nameEntry = Entry(master=nameFram)
    nameEntry.pack(side='left')
    
    # first member info part
    member1frame = Frame(master=addNewRoot, width=500, height=20, bg='#EAD7BB')
    member1frame.pack_propagate(False)
    member1frame.pack()
    member1Label = Label(master=member1frame, text='member1: ', bg = '#EAD7BB')
    member1Label.pack(side='left')
    member1Entry = Entry(master=member1frame)
    member1Entry.pack(side='left')
    
    # second member info part
    member2frame = Frame(master=addNewRoot, width=500, height=20, bg='#EAD7BB')
    member2frame.pack_propagate(False)
    member2frame.pack()
    member2Label = Label(master=member2frame, text='member2: ', bg = '#EAD7BB')
    member2Label.pack(side='left')
    member2Entry = Entry(master=member2frame)
    member2Entry.pack(side='left')
    
    # third member info part
    member3frame = Frame(master=addNewRoot, width=500, height=20, bg='#EAD7BB')
    member3frame.pack_propagate(False)
    member3frame.pack()
    member3Label = Label(master=member3frame, text='member3: ', bg = '#EAD7BB')
    member3Label.pack(side='left')
    member3Entry = Entry(master=member3frame)
    member3Entry.pack(side='left')
    
    # fourth member info part
    member4frame = Frame(master=addNewRoot, width=500, height=20, bg='#EAD7BB')
    member4frame.pack_propagate(False)
    member4frame.pack()
    member4Label = Label(master=member4frame, text='member4: ', bg = '#EAD7BB')
    member4Label.pack(side='left')
    member4Entry = Entry(master=member4frame)
    member4Entry.pack(side='left')
    
    # weight member part
    weightFrame = Frame(master=addNewRoot, width=500, height=20, bg='#EAD7BB')
    weightFrame.pack_propagate(False)
    weightFrame.pack()
    weightLabel = Label(master=weightFrame, text='weight: ', bg='#EAD7BB')
    weightLabel.pack(side='left')
    weightEntry= Entry(master=weightFrame)
    weightEntry.pack(side='left')
    
    # adding button for adding to the database
    addButton = Button(master= addNewRoot, text='add team', bd='5',  bg='#F5F7F8')
    addButton.bind('<Button>', addToDatabase)
    addButton.bind('<Enter>', lambda x: addButton.config(bg='#495E57'))
    addButton.bind('<Leave>', lambda x: addButton.config(bg='#F5F7F8'))
    addButton.pack()
    

    addNewRoot.mainloop()
    
    
def mainPage():
    """_summary_
        this will show us main page that we can add update and show score board button in this part
    """
    # main page root
    mainPageRoot = Tk()
    # main page title
    mainPageRoot.title('mainpage')
    # main page icon
    mainPageRoot.iconbitmap('icons\\mainpage.ico')
    
    # my background color
    mainPageRoot.configure(bg='#F4CE14')
    
    # size of the main page
    w = 500
    h = 500
    sw = mainPageRoot.winfo_screenwidth()
    sh = mainPageRoot.winfo_screenheight()
    x = (sw/2) - (w/2)
    y = (sh/2) - (h/2)
    
    # set geometry of the main page
    mainPageRoot.geometry('%dx%d+%d+%d'%(w,h,x,y))

    # our add new person button
    addNewButton = Button(master= mainPageRoot, text='new team', bd='5', width=10, height=2, bg='#F5F7F8')
    addNewButton.bind('<Button>', addnewTeam)
    addNewButton.bind('<Enter>', lambda x: addNewButton.config(bg='#495E57'))
    addNewButton.bind('<Leave>', lambda x: addNewButton.config(bg='#F5F7F8'))
    addNewButton.pack()
    

    # main loop of the main page
    mainPageRoot.mainloop()



mainPage()








