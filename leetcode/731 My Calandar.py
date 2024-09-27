def overlap(a, b, c, d):
    return max(a, c), min(b, d)
    
class MyCalendarTwo:

    def __init__(self):
        self.arr = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for a,b in self.overlap:
            x, y = overlap(a,b, start, end)
            if x < y:
                return False
        
        for a, b in self.arr:
            x, y = overlap(a,b, start, end)
            if x >= y:
                continue
            self.overlap.append([x, y])
        self.arr.append([start, end])
        return True
