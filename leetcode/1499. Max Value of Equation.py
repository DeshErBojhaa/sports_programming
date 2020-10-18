# 1499. Max Value of Equation
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -math.inf
        q = collections.deque()
        
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            
            if q:
                ans = max(ans, x + y + q[0][0])
            
            while q and q[-1][0] <= y - x:
                q.pop()
                
            q.append((y - x, x))
            
        
        return ans
