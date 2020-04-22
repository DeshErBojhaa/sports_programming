from collections import defaultdict
from queue import SimpleQueue
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0]:
            return False
        
        R, C = len(maze), len(maze[0])
        
        s = set(tuple(start))
        q = SimpleQueue()
        q.put(start)
        
        def add_queue(r, c):
            tup = (r,c)
            if tup in s:
                return
            q.put(tup)
            s.add(tup)
        
        while q.qsize():
            r, c = q.get()
            if tuple(destination) == (r,c):
                return True
            
            # Go left
            for i in range(c-1, -2, -1):
                if i == -1 or maze[r][i] == 1:
                    add_queue(r, 0 if i == -1 else i+1)
                    break
            
            # Go right
            for i in range(c+1, C+1):
                if i == C or maze[r][i] == 1:
                    add_queue(r, C-1 if i == C else i-1)
                    break
            
            # Go up
            for i in range(r-1, -2, -1):
                if i == -1 or maze[i][c] == 1:
                    add_queue(0 if i == -1 else i+1, c)
                    break
                    
            # Go down
            for i in range(r+1, R+1):
                if i == R or maze[i][c] == 1:
                    add_queue(R-1 if i == R else i-1, c)
                    break
        return False
