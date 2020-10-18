from queue import PriorityQueue
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = PriorityQueue()
        for s in sticks:
            pq.put(s)
        
        ans = 0
        while pq.qsize() > 1:
            a = pq.get()
            b = pq.get()
            
            ans += a+b
            
            pq.put(a+b)
        
        return ans
        
