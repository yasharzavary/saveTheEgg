from tkinter import *
from dataBase import addNewOne, getData
from functools import partial

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
        name = nameEntry.get()
        member1 = member1Entry.get()
        member2 = member2Entry.get()
        member3 = member3Entry.get()
        member4 = member4Entry.get()
        weight = weightEntry.get()
        addNewOne(name, weight, member1, member2, member3, member4)

        
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

def updateTeam(event):
    """_summary_
        this will update one team's info
    """
    def updateOne(name):
        """_summary_
            update panel of one team that we can change one teams info after comp
        """
        def change(event):
            pass
        # our changing(update) info part
        teamInfoPage = Tk()
        teamInfoPage.geometry('%dx%d+%d+%d'%(300,300,100,300))
        teamInfoPage.title('update info')
        teamInfoPage.iconbitmap('icons\\info.ico')
        
        # say that we wanna to cahnge who?
        whoLabel = Label(master=teamInfoPage, text=f'you are changing info of the team {name}')
        whoLabel.pack()
        
        # time part
        timeFrame = Frame(master=teamInfoPage, width=300, height=20)
        timeFrame.pack_propagate(False)
        timeFrame.pack(side='top')
        timeLabel = Label(master=timeFrame, text='time amount: ')
        timeLabel.pack(side='left')
        timeEntry = Entry(master=timeFrame)
        timeEntry.pack(side='left')

        # creativity part
        creativeFrame = Frame(master=teamInfoPage, width=300, height=20)
        creativeFrame.pack_propagate(False)
        creativeFrame.pack(side='top')
        cretiveLabel = Label(master=creativeFrame, text='creativity score: ')
        cretiveLabel.pack(side='left')
        creativeEntry = Entry(master=creativeFrame)
        creativeEntry.pack(side='left')       

        # egg come out or not?
        eggComeFrame = Frame(master=teamInfoPage, width=300, height=20)
        eggComeFrame.pack_propagate(False)
        eggComeFrame.pack(side='top')
        eggComeLabel = Label(master=eggComeFrame, text='egg come our?: ')
        eggComeLabel.pack(side='left')
        eggComeEntry = Entry(master=eggComeFrame)
        eggComeEntry.pack(side='left')   

        # land part
        whereComeFrame = Frame(master=teamInfoPage, width=300, height=20)
        whereComeFrame.pack_propagate(False)
        whereComeFrame.pack(side='top')
        whereComeLabel = Label(master=whereComeFrame, text='where egg land?: ')
        whereComeLabel.pack(side='left')
        whereComeEntry = Entry(master=whereComeFrame)
        whereComeEntry.pack(side='left')          

        # EIF part
        EIFFrame = Frame(master=teamInfoPage, width=300, height=20)
        EIFFrame.pack_propagate(False)
        EIFFrame.pack(side='top')
        EIFLabel = Label(master=EIFFrame, text='broke/intact/cracked: ')
        EIFLabel.pack(side='left')
        EIFEntry = Entry(master=EIFFrame)
        EIFEntry.pack(side='left')   
        
        # button of the update part
        updateBut = Button(master=teamInfoPage, text='update')
        updateBut.bind('<Button>', )
         
        # mainloop of the Tk  
        teamInfoPage.mainloop()
        
    # update page gui
    updatePage = Tk()
    updatePage.title('update team info')
    updatePage.iconbitmap('icons\\update.ico')
    updatePage.geometry('%dx%d+%d+%d'%(1200,500,200,0))
    
    # get data of the database
    data=getData()
    # make frames for better usage
    frame1 = Frame(master=updatePage, width=400, height=500, bg='#DDF2FD')
    frame1.pack_propagate(False)
    frame1.pack(side='left')
    frame2 = Frame(master=updatePage, width=400, height=500, bg='#9BBEC8')
    frame2.pack_propagate(False)
    frame2.pack(side='left')   
    frame3 = Frame(master=updatePage, width=400, height=500, bg='#427D9D')
    frame3.pack_propagate(False)
    frame3.pack(side='left') 
    
    # get name of the teams
    teamNames = [team[1] for team in data]
    
    # button part that make buttons of the teams for us
    if len(data) <= 15:
        for i in range(len(teamNames)):
            nameTemp = teamNames[i]
            butFunc = partial(updateOne, nameTemp)
            button = Button(master=frame1, text=nameTemp, command=butFunc)
            button.pack()
    elif len(data) <=30:
        for i in range(15):
            nameTemp = teamNames[i]
            butFunc = partial(updateOne, nameTemp)
            button = Button(master=frame1, text=nameTemp, command=butFunc)
            button.pack()
        
        for i in range(15, len(teamNames)):
            nameTemp = teamNames[i]
            butFunc = partial(updateOne, nameTemp)
            button = Button(master=frame2, text=nameTemp, command=butFunc)
            button.pack()   
    else:
        for i in range(15):
            nameTemp = teamNames[i]
            butFunc = partial(updateOne, nameTemp)
            button = Button(master=frame1, text=nameTemp, command=butFunc)
            button.pack()
        
        for i in range(15, 30):
            nameTemp = teamNames[i]
            butFunc = partial(updateOne, nameTemp)
            button = Button(master=frame2, text=nameTemp, command=butFunc)
            button.pack()               
         
        for i in range(30, len(teamNames)):
            nameTemp = teamNames[i]
            butFunc = partial(updateOne, nameTemp)
            button = Button(master=frame3, text=nameTemp, command=butFunc)
            button.pack()           
         
    updatePage.mainloop()
    
    
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
    
    updateButton = Button(master= mainPageRoot, text='update', bd='5', width=10, height=2, bg='#F5F7F8')
    updateButton.bind('<Button>', updateTeam)
    updateButton.bind('<Enter>', lambda x: updateButton.config(bg='#495E57'))
    updateButton.bind('<Leave>', lambda x: updateButton.config(bg='#F5F7F8'))
    updateButton.pack()

    # main loop of the main page
    mainPageRoot.mainloop()



mainPage()








