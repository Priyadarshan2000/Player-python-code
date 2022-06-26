class Player:
    def __init__(self, playerName, team, playerType, isCaptain, runs, wickets):
        self.playerName = playerName
        self.team = team
        self.playerType = playerType
        self.isCaptain = isCaptain
        self.runs = runs
        self.wickets = wickets
    def calculatePoints(self, runs, wickets, isCaptain):
        points = 10*wickets + 1*runs
        if(isCaptain):
            points *= 2
        return points

class Tournament:
    def __init__(self, playerList):
        self.playerList = playerList
        
    def getPlayerList(self, playerType, points):
        res = []
        for p in self.playerList:
            if p.playerType == playerType and p.calculatePoints(p.runs, p.wickets, p.isCaptain)>points:
                res.append(p)
        if len(res)==0:
            return None
        return res
        
    def findPlayerPoints(self, team, points):
        res = {}
        for p in playerList:
            if p.team == team and p.calculatePoints(p.runs, p.wickets, p.isCaptain) > points:
                res[p.playerName] = p.calculatePoints(p.runs, p.wickets, p.isCaptain)
        if len(res)==0:
            return None
        return res    
        
if(__name__=="__main__"):
    playerList = []
    size = int(input())
    for i in range(0,size):
        playerName = input()
        team = input()
        playerType = input()
        isCaptain = bool(input())
        runs = int(input())
        wickets = int(input())
        pl = Player(playerName, team, playerType, isCaptain, runs, wickets)
        playerList.append(pl)
    
    t1 = Tournament(playerList)
    
    playerType = input('Enter player type : ')
    points_1 = int(input('Enter global threshold points : '))
    
    team = input('Enter player team : ')
    points_2 = int(input('Enter local threshold points : '))
    
    globalList = t1.getPlayerList(playerType, points_1)
    
    if globalList==None:
        print('Player Not Found')
    else:
        for p in globalList:
            print(p.playerName)
            print(p.runs)
            print(p.wickets)
    
    localList = t1.findPlayerPoints(team, points_2)
    
    if localList==None:
        print('Player Not Found')
    else:
        for p in localList:
            print(p.playerName)
            print(p.calculatePoints(p.runs, p.wickets, p.isCaptain))
    