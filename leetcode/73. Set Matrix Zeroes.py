# 73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_zero = not all(matrix[0])
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0]:
                continue
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for i in range(len(matrix[0])):
            if matrix[0][i]:
                continue
            for j in range(len(matrix)):
                matrix[j][i] = 0
        
        if first_row_has_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        
