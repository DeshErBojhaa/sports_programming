from queue import SimpleQueue
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = [0] * numCourses
        
        for to, frm in prerequisites:
            g[frm].append(to)
            indegree[to] += 1
        
        q = SimpleQueue()
        for i, v in enumerate(indegree):
            if not v:
                q.put(i)
        
        removed = 0
        
        while q.qsize():
            top = q.get()
            removed += 1
            for n in g[top]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.put(n)

        return removed == numCourses
