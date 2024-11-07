class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = [0] * 25
        for i in range(25):
            for c in candidates:
                cnt[i] += (c & (1<<i)) != 0
        
        return max(cnt)
