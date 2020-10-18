# 1610. Maximum Number of Visible Points
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        at_origin = 0
        p = []
        for i, (x, y) in enumerate(points):
            if [x, y] == location:
                at_origin += 1
                continue
            p.append([x - location[0], y - location[1]])
        
        points = sorted(map(lambda x: atan2(*x), p))
        points += [(pi * 2) + p0 for p0 in points]
        
        l, ans = 0, 0
        angle = radians(angle)
        
        for r, v in enumerate(points):
            while l <= r and v - points[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
        
        return ans + at_origin
