class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_half = [] # Max Heap
        self.big_half = []   # Min Heap
        self.N = 0
        

    def addNum(self, num: int) -> None:
        self.N += 1
        x = heapq.heappushpop(self.small_half,-num)
        heapq.heappush(self.big_half, -x)
        
        if len(self.big_half) > len(self.small_half):
            x = heapq.heappop(self.big_half)
            heapq.heappush(self.small_half, -x)
        

    def findMedian(self) -> float:
        if self.N % 2:
            return -self.small_half[0]
        return ((-self.small_half[0]) + self.big_half[0])/2.
