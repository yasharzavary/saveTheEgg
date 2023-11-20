from mysql.connector import Connect, Error

def getData():
    """_summary_
        this function will get us datas that exist in the database
    """
    with Connect(host='localhost', port='3306', user='root',
                password='Yasharzavary360', database='saveTheEgg') as conn:
        pointer = conn.cursor()
        pointer.execute('select * from peopleScore')
        dataList = []
        for team in pointer:
            dataList.append(team)
        return dataList

def updateFinalScores(fList):
    """_summary_
        this function change finalpoints of the compition members
    Args:
        fList(list): list of the scores
    """
    with Connect(host='localhost', port='3306', user='root',
                password='Yasharzavary360', database='saveTheEgg') as conn:
        pointer=conn.cursor()
        pointer.execute('select * from peoplescore')
        idList=[]
        for team in pointer:
            idList.append(team[0])
        for i in range(len(idList)):
            pointer.execute("update peoplescore set finalScore="+str(fList[i])+" where id="+str(idList[i]))
        conn.commit()

def updateCompData(teamName, cTime, cCreativeity, cEgg, cWhere, cEIF):
    """_summary_
        # after comp, this function will update the data of the team into the database for score calculate
    """
    with Connect(host='localhost', port='3306', user='root',
                password='Yasharzavary360', database='saveTheEgg') as conn:
        changePointer = conn.cursor()
        
        # find id of the teamName
        changePointer.execute('select * from peopleScore')
        for team in changePointer:
            if team[1] == teamName:
                findId = team[0]
        
        # info update part
        changePointer.execute('update peopleScore set timeAmount='+str(cTime)+" where id="+str(findId))
        changePointer.execute('update peopleScore set Creativity='+str(cCreativeity)+" where id="+str(findId))
        changePointer.execute('update peopleScore set eggComeOut='+str(cEgg)+" where id="+str(findId))
        changePointer.execute('update peopleScore set whereCome='+str(cWhere)+" where id="+str(findId))
        changePointer.execute('update peopleScore set EIF='+str(cEIF)+" where id="+str(findId))
        conn.commit()

def addNewOne(name, weight, member1='', member2='', member3='',member4=''):
    """_summary_
    this function will connect to the database and add one new team with team members to the database.
    Args:
        name (_type_): team name
        member1 (str, optional): first member's name
        member2 (str, optional): second member's name
        member3 (str, optional): third member's name
        member4 (str, optional): fourth member's name
    """
    try:
        with Connect(host='localhost', port='3306', user='root',
                    password='Yasharzavary360', database='saveTheEgg') as conn:
            mydata = conn.cursor()
            mydata.executemany("""insert into peopleScore (teamName, teamMember1, teamMember2, teamMember3, teamMember4, weightAmount)
                        values (%s,%s,%s,%s,%s,%s)""",[(name,member1,member2,member3,member4,weight)])
            conn.commit()
    except Error as error:
        print(error)   
        
        
          






