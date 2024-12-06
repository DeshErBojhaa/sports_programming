class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b, ans, sm = set(banned), 0, 0
        for i in range(1, n+1):
            if i in b:
                continue
            sm += i
            if sm > maxSum:
                break
            ans += 1
        return ans
