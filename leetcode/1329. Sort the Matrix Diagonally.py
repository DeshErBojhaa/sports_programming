# 1329. Sort the Matrix Diagonally
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        
        n, m = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        
        for i, j in itertools.product(range(n), range(m)):
            d[i - j].append(mat[i][j])
        
        for k in d:
            d[k].sort(reverse=True)
        
        for i, j in itertools.product(range(n), range(m)):
            mat[i][j] = d[i-j].pop()
        
        return mat
