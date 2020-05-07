# 329. Longest Increasing Path in a Matrix
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        longest_path = {}
        
        def search(i, j):
            if (i,j) in longest_path:
                return longest_path[i,j]
            
            ans = 1
            for ni, nj in ((i,j-1), (i-1,j), (i,j+1), (i+1, j)):
                if ni < 0 or ni >= len(matrix) or nj < 0 or nj >= len(matrix[0]) or matrix[i][j] >= matrix[ni][nj]:
                    continue
                ans = max(ans, search(ni, nj) + 1)
            longest_path[i,j] = ans
            return ans
        
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                ans = max(ans, search(i, j))
        
        return ans
