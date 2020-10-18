# 675. Cut Off Trees for Golf Event
from collections import defaultdict, deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        n, m = len(forest), len(forest[0])
        distance_cache = {}
        
        def go(start, end):
            if start == end:
                return 0
            
            dis = defaultdict(lambda: float('inf'))
            
            q = deque()
            q.append(start)
            dis[start] = 0
    
            while q:
                curx, cury = q.popleft()
                # print(curx, cury)
                for dx, dy in zip((0,-1,0,1), (-1,0,1,0)):
                    nx, ny = curx+dx, cury+dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or (nx,ny) in dis:
                        continue
                    if forest[nx][ny] == 0:
                        continue
                        
                    if (nx, ny) == end:
                        return dis[curx, cury] + 1
                    dis[nx,ny] = dis[curx, cury] + 1
                    q.append((nx, ny))
            
            return -1
        
        trees = sorted([(v,r,c) for r, row in enumerate(forest) for c, v in enumerate(row) if v > 1])
        
        ans = 0
        start = (0,0)
        for _, i, j in trees:
            dis = go(start, (i,j))
            if dis == -1:
                return -1
            ans += dis
            start = (i,j)
        
        return ans
        
# [[1,2,3],[0,0,4],[7,6,5]]        
        
# 2, 4, 6, 8, 10,12
# 0, 0, 0, 0,  0,14
# 15,16,17,18,19,20
# 13, 0, 0, 0, 0, 0
# 11, 9, 7, 5, 3, 1

# 2, 4, 6, 8
# 0, 0, 0, 9
# 1, 3, 5, 7
