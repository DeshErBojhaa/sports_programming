# 1218. Longest Arithmetic Subsequence of Given Difference
class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        d = {}
        for v in arr:
            d[v] = d.get(v-diff, 0) + 1
        
        return max(d.values())
