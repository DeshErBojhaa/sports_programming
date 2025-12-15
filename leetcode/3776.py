class Solution:
    def minMoves(self, bal: List[int]) -> int:
        if sum(bal) < 0:
            return -1
        N = len(bal)
        idx = next((i for i, x in enumerate(bal) if x < 0), None)
        if idx is None:
            return 0
        ans = 0
        for d in range(1, N):
            li = (idx - d) % N
            left = min(abs(bal[idx]), bal[li])
            bal[idx] += left
            bal[li] -= left
            ans += left * d
            if bal[idx] == 0:
                break
            
            ri = (idx + d) % N
            right = min(abs(bal[idx]), bal[ri])
            bal[idx] += right
            bal[ri] -= right
            ans += right * d
            if bal[idx] == 0:
                break
        
        return ans
