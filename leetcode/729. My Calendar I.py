# 729. My Calendar I
from bisect import bisect_left
class MyCalendar:

    def __init__(self):
        self.data = []

    def book(self, start: int, end: int) -> bool:
        if not self.data:
            self.data.append([start, end])
            return True
        
        ind = bisect_left([x[0] for x in self.data], end)
        # print(f'{start, end}, {[x[0] for x in self.data]}, index {ind}')
        if ind == len(self.data):
            if self.data[-1][1] > start:
                return False
            self.data.append([start, end])
            return True
        if ind == 0:
            if self.data[0][0] >= end:
                self.data = [[start, end]] + self.data
                return True
            return False
        
        if end <= self.data[ind][0] and self.data[ind-1][1] <= start:
            self.data = self.data[:ind] + [[start, end]] + self.data[ind:]
            return True
        return False
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
