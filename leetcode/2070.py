class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        d = defaultdict(lambda: -1)
        for a, b in items:
            d[a] = max(d[a], b)
        d = sorted(d.items(), key=lambda a: a[0])
        mx = -inf
        for i in range(len(d)):
            mx = max(mx, d[i][1])
            d[i] = (d[i][0], mx)
            
        ans = []
        for q in queries:
            idx = bisect_left(d, (q, 0))
            if idx >= len(d) or (q < d[idx][0] and idx):
                idx -= 1
            
            if q >= d[idx][0]:
                ans.append(d[idx][1])
            else:
                ans.append(0)
        return ans
