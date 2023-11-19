from tkinter import *




def mainPage():
    # main page root
    mainPageRoot = Tk()
    # main page title
    mainPageRoot.title('mainpage')
    # main page icon
    mainPageRoot.iconbitmap('icons\\mainpage.ico')
    
    # size of the main page
    w = 500
    h = 500
    sw = mainPageRoot.winfo_screenwidth()
    sh = mainPageRoot.winfo_screenheight()
    x = (sw/2) - (w/2)
    y = (sh/2) - (h/2)
    
    # set geometry of the main page
    mainPageRoot.geometry('%dx%d+%d+%d'%(w,h,x,y))




    # main loop of the main page
    mainPageRoot.mainloop()



mainPage()








