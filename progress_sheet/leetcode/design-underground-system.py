from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.checked_in = defaultdict(list)
        self.checked_out = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] =[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        star,start_time=self.checked_in[id]
        self.checked_out[(star,stationName)].append(t-start_time)
       
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        temp=self.checked_out[(startStation,endStation)]
        if temp:
            return sum(temp)/len(temp)
        return 0.0    
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
