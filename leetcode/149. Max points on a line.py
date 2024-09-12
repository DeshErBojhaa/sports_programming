class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3 :
            return len(points)

        def slop(x1, y1, x2, y2):
            return (y2 - y1) / (x2 - x1) if x2 != x1 else inf
        
        ans = 0
        for i, (x1, y1) in enumerate(points):
            dic = defaultdict(lambda: 1)
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                slp1 = slop(x1, y1, x2, y2)
                dic[slp1] += 1
            ans = max(ans, max(dic.values()))
        
        return ans
