class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        notDead = [1]* len(senate)
        
        def checknotDead(notDead, senate):
            r_notDead = False
            d_notDead = False
            for i in range(len(senate)):
                if(notDead[i] == 1 and senate[i] == "R"):
                    r_notDead= True
                if(notDead[i] == 1 and senate[i] == "D"):
                    d_notDead= True
            return d_notDead and r_notDead
        
        def WhoWon(notDead,senate):
            r_notDead = False
            d_notDead = False
            for i in range(len(senate)):
                if(notDead[i] == 1 and senate[i] == "R"):
                    return "Radiant"
                if(notDead[i] == 1 and senate[i] == "D"):
                    return "Dire"
            return ""
        q = []
        while checknotDead(notDead, senate):
            
            for i in range(len(senate)):
                if(len(q)> 0):
                    if(q[0] == senate[i] and notDead[i] == 1):
                        q.pop(0)
                        notDead[i]=0
                if(notDead[i] == 1):
                    if(senate[i]== "R"):
                        q.append("D")
                    else:
                        q.append("R")
        return WhoWon(notDead, senate)
        