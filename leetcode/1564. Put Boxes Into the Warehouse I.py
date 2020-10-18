# 1564. Put Boxes Into the Warehouse I
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], wh: List[int]) -> int:
        N, ans = len(boxes), 0
        boxes.sort()
        
        for i in range(N-1,-1,-1):
            if boxes[i] <= wh[ans]:
                ans += 1
        
        return ans
