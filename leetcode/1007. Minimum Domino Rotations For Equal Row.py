# 1007. Minimum Domino Rotations For Equal Row
from functools import lru_cache
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        
        def check(x):
            rotate_a, rotate_b = 0, 0
            
            for i in range(N):
                if A[i] != x and B[i] != x:
                    return -1
                if A[i] != x:
                    rotate_a += 1
                if B[i] != x:
                    rotate_b += 1
                
            return min(rotate_a, rotate_b)
        
        rotate = check(A[0])
        if rotate != -1:
            return rotate
        return check(B[0])
