from collections import defaultdict
from queue import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        s = set(range(numCourses))
        g = defaultdict(list)
        indeg = defaultdict(int)
        ans = []
        for cur, par in prerequisites:
            g[par].append(cur)
            s.discard(cur)
            indeg[cur] += 1
        
        q = deque(s)
        
        while q:
            top = q.popleft()
            ans.append(top)
            
            for x in g[top]:
                indeg[x] -= 1
                if indeg[x] == 0:
                    q.append(x)
        
        if len(ans) == numCourses:
            return ans
        return []
