from tkinter import *
from dataBase import getData

def showScoreBoard(event):
    """_summary_
        this function will show us score board of the compition
    """
    def addTeams():
        data = getData()
        data=sorted(data, key=lambda x: x[14], reverse=True)
        for i in range(len(data)):
            if i == 0 or i == 1 or i == 2:
                head1 = Label(scoreFrame, text=data[i][1] , width=25, height = 5, relief='solid', bg='#C7DCA7')
                head1.grid(row=i+1, column=7)
                head2 = Label(scoreFrame, text=data[i][6], width=25, height = 5, relief='solid', bg='#C7DCA7')
                head2.grid(row=i+1, column=6)
                head3 = Label(scoreFrame, text=data[i][8], width=25, height = 5 , relief='solid', bg='#C7DCA7')
                head3.grid(row=i+1, column=5)
                head4 = Label(scoreFrame, text=data[i][10], width=25, height = 5 , relief='solid', bg='#C7DCA7')
                head4.grid(row=i+1, column=4)
                head5 = Label(scoreFrame, text=data[i][11], width=25, height = 5 , relief='solid', bg='#C7DCA7')
                head5.grid(row=i+1, column=3)
                head6 = Label(scoreFrame, text=data[i][12], width=25, height = 5 , relief='solid', bg='#C7DCA7')
                head6.grid(row=i+1, column=2)
                head7 = Label(scoreFrame, text=data[i][13], width=25, height = 5 , relief='solid', bg='#C7DCA7')
                head7.grid(row=i+1, column=1)
                head8 = Label(scoreFrame, text=data[i][14], width=25, height = 5 , relief='solid', bg='#C7DCA7')
                head8.grid(row=i+1, column=0)
            else:
                head1 = Label(scoreFrame, text=data[i][1], width=25, height = 5, relief='solid')
                head1.grid(row=i+1, column=7)
                head2 = Label(scoreFrame, text=data[i][6], width=25, height = 5, relief='solid')
                head2.grid(row=i+1, column=6)
                head3 = Label(scoreFrame, text=data[i][8], width=25, height = 5 , relief='solid')
                head3.grid(row=i+1, column=5)
                head4 = Label(scoreFrame, text=data[i][10], width=25, height = 5 , relief='solid')
                head4.grid(row=i+1, column=4)
                head5 = Label(scoreFrame, text=data[i][11], width=25, height = 5 , relief='solid')
                head5.grid(row=i+1, column=3)
                head6 = Label(scoreFrame, text=data[i][12], width=25, height = 5 , relief='solid')
                head6.grid(row=i+1, column=2)
                head7 = Label(scoreFrame, text=data[i][13], width=25, height = 5 , relief='solid')
                head7.grid(row=i+1, column=1)
                head8 = Label(scoreFrame, text=data[i][14], width=25, height = 5 , relief='solid')
                head8.grid(row=i+1, column=0)
    
    # my score board gui
    scoreShedule = Tk()
    scoreShedule.geometry("%dx%d+%d+%d"%(1500, 900, 0, 0))
    scoreShedule.title('scoreBoard')
    scoreShedule.attributes('-fullscreen',True)
    scoreShedule.iconbitmap('icons\\scoreBoard.ico')

    scoreShedule.configure(bg='#F9F3CC')
    
    # frma of the score board
    scoreFrame= Frame(master=scoreShedule)
    scoreFrame.pack()

    # headers of the shedule
    head1 = Label(scoreFrame, text='نام تیم', width=25, height = 5, relief='solid', bg='#D2E0FB')
    head1.grid(row=0, column=7)
    head2 = Label(scoreFrame, text='زمان', width=25, height = 5, relief='solid', bg='#D2E0FB')
    head2.grid(row=0, column=6)
    head3 = Label(scoreFrame, text='وزن', width=25, height = 5 , relief='solid', bg='#D2E0FB')
    head3.grid(row=0, column=5)
    head4 = Label(scoreFrame, text='خلاقیت', width=25, height = 5 , relief='solid', bg='#D2E0FB')
    head4.grid(row=0, column=4)
    head5 = Label(scoreFrame, text='خروج تخم مرغ', width=25, height = 5 , relief='solid', bg='#D2E0FB')
    head5.grid(row=0, column=3)
    head6 = Label(scoreFrame, text='محل سقوط', width=25, height = 5 , relief='solid', bg='#D2E0FB')
    head6.grid(row=0, column=2)
    head7 = Label(scoreFrame, text='سالم/شکسته/ترک', width=25, height = 5 , relief='solid', bg='#D2E0FB')
    head7.grid(row=0, column=1)
    head8 = Label(scoreFrame, text='امتیاز نهایی', width=25, height = 5 , relief='solid', bg='#D2E0FB')
    head8.grid(row=0, column=0)
    
    addTeams()
    scoreShedule.mainloop()
