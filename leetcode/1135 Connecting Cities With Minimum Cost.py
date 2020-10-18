# 1135. Connecting Cities With Minimum Cost
from queue import PriorityQueue
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        parent = list(range(N+1))
        
        def find_parent(u):
            while parent[u] != u:
                u = parent[u]
            return parent[u]
        
        pq = PriorityQueue()
        
        for conn in connections:
            pq.put((conn[2], conn[0], conn[1]))
        
        ans, connected = 0, 0
        while pq.qsize():
            cost, a, b = pq.get()
            if find_parent(a) != find_parent(b):
                connected += 1
                ans += cost
                parent[find_parent(a)] = find_parent(b)
        
        return ans if connected == N-1 else -1
