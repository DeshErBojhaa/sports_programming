# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc = sorted([0] + hc + [h])
        vc = sorted([0] + vc + [w])
        
        maxx = 0
        for i in range(1, len(hc)):
            maxx = max(maxx, hc[i] - hc[i-1])
        maxy = 0
        for i in range(1, len(vc)):
            maxy = max(maxy, vc[i] - vc[i-1])
        
        return (maxx * maxy) % ((10**9) + 7)
