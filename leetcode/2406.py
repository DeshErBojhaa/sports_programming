class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ans = 1
        arr = []
        for a, b in intervals:
            arr.append([a, -1])
            arr.append([b, 1])
        arr.sort()
        cum = 0
        for a, x in arr:
            cum += (-x)
            ans = max(ans, cum)
            
        return ans
