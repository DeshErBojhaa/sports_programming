from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = PriorityQueue()
        for i in stones:
            pq.put(-i)
        while pq.qsize() >= 2:
            a = -pq.get()
            b = -pq.get()
            
            if a == b:
                continue
            pq.put(-(a-b))
        if not pq.qsize():
            return 0
        return -pq.get()
