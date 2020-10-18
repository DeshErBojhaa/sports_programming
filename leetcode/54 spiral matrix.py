class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        R, C = len(matrix), len(matrix[0])
        ans = []
        l, r, u, d = 0, C-1, 0, R-1
        while u <= d and l <= r:
            for rot in range(4):
                if rot == 0:   # Left -> Right
                    # print('>', l, r+1)
                    for i in range(l, r+1, 1):
                        ans.append(matrix[u][i])
                    u += 1
                    if len(ans) == R*C:
                        break
                elif rot == 1:  # Top -> Down
                    for i in range(u, d+1, 1):
                        ans.append(matrix[i][r])
                    r -= 1
                    if len(ans) == R*C:
                        break
                elif rot == 2:  # Right -> Left
                    for i in range(r, l-1, -1):
                        ans.append(matrix[d][i])
                    d -= 1
                    if len(ans) == R*C:
                        break
                elif rot == 3:  # Down -> Top
                    for i in range(d, u-1, -1):
                        ans.append(matrix[i][l])
                    l += 1
                    if len(ans) == R*C:
                        break
        return ans
