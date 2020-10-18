class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                
        ans = any(matrix[0])
        ans = max(ans, any(r[0] for r in matrix))
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][j]:
                    continue
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                ans = max(ans, matrix[i][j])
        
        return ans * ans
