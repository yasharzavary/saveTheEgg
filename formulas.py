from dataBase import getData

def weightScore(wList):
    print(wList)
    maxW = max(wList)
    minW = min(wList)
    if maxW == minW:return [0]*len(wList)
    wDiff = (maxW-minW)
    return [200*(maxW - cW)/wDiff for cW in wList]

        


def calculateScore():
    data = getData()
    if len(data)>1:
        wScore = weightScore([team[9] for team in data])
        


calculateScore()