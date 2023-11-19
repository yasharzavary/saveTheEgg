from dataBase import getData

def weightScore(wList):
    """_summary_
        this function will calculate weight score with formula that it given
    Args:
        wList(list): list of the weights
    """
    # find max and min weight from the data
    maxW = max(wList)
    minW = min(wList)
    # if these two is similar, return one zero based list
    if maxW == minW: return [0]*len(wList)
    # find diff between max and min weight
    wDiff = (maxW-minW)
    # return weight scores
    return [200*(maxW - cW)/wDiff for cW in wList]

def timeScore(tList):
    """_summary_
        this function will calculate time score with formula that it given
    Args:
        tlist(list): list of the times
    """
    # find max and min time of the data
    maxT = max(tList)
    minT = min(tList)
    # if max and min time is simalar, it will return one zero based list
    if maxT == minT: return [0]*len(wList)
    # find diff between max and min time
    tDiff = (maxT - minT)
    # return time scores
    return [100*(maxT - cT)/tDiff for cT in tList]    


def calculateScore():
    """_summary_
        main function that get scores from the database and calculate the final score from that
    """
    # get datas from the database
    data = getData()
    # if we have two or above person, it will calculate scores
    if len(data)>1:
        # find basic scores from the datas
        wScore = weightScore([team[9] for team in data])
        tScore = timeScore([team[6] for team in data]) 
        createvity = [team[11] for team in data]
        outScore = [team[12]*250 for team in data]
        grandScore = [team[13]*25 for team in data]
        EIF = [team[14] for team in data]
        # calculate final score depend on the mian formula
        finalScore = [(outScore[i]+wScore[i]+tScore[i]+grandScore[i])*EIF[i] + createvity[i] for i in range(len(data))]
        # send finalscores to the show score part
        return 
        
        
calculateScore()
