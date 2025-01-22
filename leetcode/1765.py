class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        N, M = len(isWater), len(isWater[0])
        q = deque()
        ans = [[None]*M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                if isWater[i][j]:
                    ans[i][j] = 0
                    q.append([i, j, 0])
        
        while q:
            x, y, cost = q.popleft()
            for nx, ny in [[x+1, y], [x-1,y], [x,y+1], [x,y-1]]:
                if not 0 <= nx < N or not 0 <= ny < M or ans[nx][ny] is not None:
                    continue
                ans[nx][ny] = cost + 1
                q.append([nx, ny, cost + 1])
        
        return ans
