# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:




class Solution:
    def find(self, bm, l, r, row):
        if l < 0 or l > r:
            return float('inf')

        mid = (r + l) // 2
        
        for i in range(row):
            val = bm.get(i, mid)
            if val == 1:
                return min(mid, self.find(bm, l, mid-1, row))
        return self.find(bm, mid+1, r, row)
        
        
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        ans = self.find(binaryMatrix, 0, C-1, R)
        return -1 if ans > 10000 else ans
        
