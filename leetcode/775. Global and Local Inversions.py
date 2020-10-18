# 775. Global and Local Inversions
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        min_sofar = N
        
        for i in range(N-1, -1, -1):
            min_sofar = min(min_sofar, A[i])
            if i-2 >= 0 and A[i-2] > min_sofar:
                return False
        return True
