# 311. Sparse Matrix Multiplication
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ra, ca = len(A), len(A[0])
        rb, cb = len(B), len(B[0])
        
        ans = [[0]* cb for _ in range(ra)]
        
        for i in range(ra):
            for j in range(ca):
                for k in range(cb):
                    ans[i][k] += A[i][j] * B[j][k]
        
        return ans
