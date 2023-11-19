from mysql.connector import Connect, Error

def getData():
    with Connect(host='localhost', port='3306', user='root',
                password='Yasharzavary360', database='saveTheEgg') as conn:
        pointer = conn.cursor()
        pointer.execute('select * from peopleScore')
        dataList = []
        for team in pointer:
            dataList.append(team)
        return dataList

def update():
    pass

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
        
        
          






