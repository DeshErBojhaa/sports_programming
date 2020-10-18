
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0
        if len(A) < 2:
            return len(A)
        
        starting_ind = 0
        ans = 1
        for i in range(1, len(A)):
            c = (A[i-1] > A[i]) - (A[i-1] < A[i])  # Compare A[i-1] with A[i]
            if c == 0:
                starting_ind = i
            elif i == len(A) - 1 or (c * ((A[i]>A[i+1]) - (A[i]<A[i+1]))) != -1:
                ans = max(ans, i - starting_ind + 1)
                starting_ind = i
        return ans
