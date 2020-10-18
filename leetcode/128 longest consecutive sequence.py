class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        ans = 0
        s = set(n)
        for x in s:
            # Check if this is the beginning of the series
            if x-1 in s:
                continue
            y = x+1
            while y in s:
                y += 1
            ans = max(ans, y-x)
        return ans
