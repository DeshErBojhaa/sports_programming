class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        found = False
        row, col = len(matrix), len(matrix[0])
        
        def search(r, c, R, C):
            if r < 0 or c < 0 or R >= row or C >= col or r > R or c > C:
                return
            nonlocal found
            if found:
                return
            
            midr = (R + r) // 2
            midc = (C + c) // 2
            
            if matrix[midr][midc] == target:
                found = True
                return
            
            if matrix[midr][midc] > target:
                search(midr, c, midr, midc-1)
                search(r, c, midr-1, C)
            else:
                search(midr, midc+1, midr, C)
                search(midr+1, c, R, C)
            return
        
        search(0, 0, row-1, col-1)
        return found
