# 857. Minimum Cost to Hire K Workers
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        arr = sorted((w/q, q, w) for w, q in zip(wage, quality))
        heap = []
        sumq, ans = 0, math.inf
        
        for f, q, w in arr:
            sumq += q
            heappush(heap, -q)
            
            if len(heap) > K:
                sumq += heappop(heap)
            
            if len(heap) == K:
                ans = min(ans, sumq * f)
        
        return ans
