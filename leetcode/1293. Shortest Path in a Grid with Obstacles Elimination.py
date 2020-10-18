# 1293. Shortest Path in a Grid with Obstacles Elimination
from collections import defaultdict, deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        N, M = len(grid), len(grid[0])
        if k >= N + M - 3:
            return N + M -2
        dist = defaultdict(lambda: float('inf'))
        q = deque([(0,0,k)])
        dist[0,0,k] = 0
        
        while q:
            x, y, rem = q.pop()
            for nx, ny in zip([x, x-1, x, x+1], [y-1, y, y+1, y]):
                if not N > nx >= 0 <= ny < M:
                    continue
                state = nx, ny, rem - grid[nx][ny]
                if rem - grid[nx][ny] < 0:
                    continue
                if dist[state] > dist[x, y, rem] + 1:
                    dist[state] = dist[x, y, rem] + 1
                    q.append((state))
        
        ans = float('inf')
        
        for i in range(k+1):
            ans = min(ans, dist[N-1, M-1, i])
        
        return ans if ans < float('inf') else -1

