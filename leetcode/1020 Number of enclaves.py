def numEnclaves(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        
        def fill(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or not A[i][j]:
                return
            
            A[i][j] = 0
            
            fill(i+1, j)
            fill(i-1, j)
            fill(i, j+1)
            fill(i, j-1)
        
        for i in range(n):
            fill(i, 0)
            fill(i, m-1)
        
        for j in range(m):
            fill(0, j)
            fill(n-1, j)
        
        ans = 0
        for i in range(n):
            ans += A[i].count(1)
        
        return ans
