from tkinter import *


def addnewTeam(event):
    pass

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








