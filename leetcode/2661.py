class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        N = len(arr)
        for i in range(N):
            arr[i] -= 1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] -= 1
    
        def ok(idx):
            seen = [False] * N
            for x in arr[:idx]:
                seen[x] = True
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    v = mat[i][j]
                    if not seen[v]:
                        break
                else:
                    return True
            
            for j in range(len(mat[0])):
                for i in range(len(mat)):
                    v = mat[i][j]
                    if not seen[v]:
                        break
                else:
                    return True
            
            return False
        
        lo, hi = 0, N
        while lo < hi:
            mid = (lo + hi) // 2
            if not ok(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
