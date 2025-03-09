class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        cnt, ans = 1, 0
        colors += colors[:k-1]
        for i, c in enumerate(colors[1:], 1):
            if colors[i-1] != c:
                cnt += 1
            else:
                cnt = 1
            ans += (cnt >= k)

        return ans
