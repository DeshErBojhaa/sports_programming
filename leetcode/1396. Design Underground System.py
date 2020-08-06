# 1396. Design Underground System
class UndergroundSystem:

    def __init__(self):
        self.recent_entry = {}
        self.data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.recent_entry[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, tm = self.recent_entry[id]
        cnt, tot_tm = self.data.get((station, stationName), (0, 0))
        
        tot_tm += (t - tm)
        cnt += 1
        
        self.data[station, stationName] = (cnt, tot_tm)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cnt, tm = self.data[startStation, endStation]
        return tm/cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
