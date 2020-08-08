# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
from collections import defaultdict, deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dist = [[float('inf')] * M for _ in range(N)]
        dist[0][0] = 0
        q = deque([(0,0,0)])
        
        # 1 ->
        # 2 <-
        # 3 V
        # 4 ^
        
        def direction_changed(a,b, c,d):
            sign = grid[a][b]
            if sign == 1 and a == c and b+1 == d:
                return 0
            if sign == 2 and a == c and b-1 == d:
                return 0
            if sign == 3 and a+1 == c and b == d:
                return 0
            if sign == 4 and a-1 == c and b== d:
                return 0
            return 1
            
        
        while q:
            x, y, cost = q.popleft()
            for nx, ny in zip([x, x+1, x, x-1], [y+1, y, y-1, y]):
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                new_cost = cost + direction_changed(x,y, nx,ny)
                
                if dist[nx][ny] > new_cost:
                    dist[nx][ny] = new_cost
                    if new_cost > cost:
                        q.append((nx, ny, new_cost))
                    else:
                        q.appendleft((nx, ny, new_cost))
        
        return dist[-1][-1]
