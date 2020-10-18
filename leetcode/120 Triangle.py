# 120. Triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i+1):
                cur_min = float('inf')
                if j < i:
                    cur_min = min(cur_min, triangle[i-1][j])
                if j - 1 >=0:
                    cur_min = min(cur_min, triangle[i-1][j-1])
                    
                triangle[i][j] += cur_min
        
        return min(triangle[-1])
