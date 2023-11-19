from mysql.connector import Connect, Error


def update():
    pass

def addNewOne(name, member1='', member2='', member3='',member4='', ):
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
            mydata.execute(f'''insert into mydata (name, member1, member2, member3, member4)
                        values ({name}, {member1}, {member2}, {member3}, {member4})''')
            conn.commit()
    except Error as error:
        print(error.message)
        
        






