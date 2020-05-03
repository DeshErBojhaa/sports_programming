from collections import defaultdict, deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        distance = [defaultdict(int) for _ in range(2)]
        q = [deque() for _ in range(2)]
        
        distance[0][0,0] = 0
        distance[1][x,y] = 0
        
        q[0].append((0,0))
        q[1].append((x,y))
        
        active_ind = 0
        
        while any(map(len, q)):
            active_q = q[active_ind]
            active_dis = distance[active_ind]
            passive_dis = distance[1 - active_ind]
            
            cur_x, cur_y = active_q.popleft()
            
            
            for dx, dy in zip((1,2,2,1,-1,-2,-2,-1), (-2,-1,1,2,2,1,-1,-2)):
                nx, ny = cur_x + dx, cur_y + dy
                
                if (nx, ny) in passive_dis:
                    return active_dis[cur_x, cur_y] + passive_dis[nx, ny] + 1
                if (nx, ny) in active_dis:
                    continue
                if abs(nx) > abs(x) + 20 or abs(ny) > abs(y) + 20:
                    continue
                    
                active_dis[nx, ny] = active_dis[cur_x, cur_y] + 1
                active_q.append((nx, ny))
            active_ind = 1 - active_ind
        
        return min(distance[0][x,y], distance[1][0,0])
