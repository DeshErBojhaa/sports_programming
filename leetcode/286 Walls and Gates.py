# 286. Walls and Gates
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        INF = (2**31) -1
        q = deque()
        
        for i, row in enumerate(rooms):
            for j, v in enumerate(row):
                if v == 0:
                    q.append((i,j))
        
        while q:
            i, j = q.popleft()
            for ni, nj in ((i,j-1), (i-1,j), (i, j+1), (i+1,j)):
                if ni < 0 or ni >= len(rooms) or nj < 0 or nj >= len(rooms[0]) or rooms[ni][nj]!= INF:
                    continue
                rooms[ni][nj] = rooms[i][j] + 1
                q.append((ni,nj))
