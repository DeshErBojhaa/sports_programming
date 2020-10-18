# 685. Redundant Connection II
from collections import defaultdict
class Solution:
    def rooted_graph(self, root, g, edges):
        flag = [False] * (self.N + 1)
        
        def visit(cur, a, b):
            flag[cur] = True
            cnt = 1
            for nxt in g[cur]:
                if flag[nxt] or (cur == a and nxt == b):
                    continue
                cnt += visit(nxt, a, b)
            return cnt
        
        for a, b in reversed(edges):
            if visit(root, a, b) == self.N:
                return [a, b]
            flag = [False] * (self.N + 1)
        return [None, None]
        
    
    def find_cycle(self, g):
        onstack, t = [False] * (self.N + 1), 0
        explore_time, backedge = [None] * (self.N + 1), [None] * (self.N + 1)
        scc = []
        
        def dfs(cur, stack):
            nonlocal t
            t += 1
            explore_time[cur] = backedge[cur] = t
            onstack[cur] = True
            stack.append(cur)
            
            for nxt in g[cur]:
                if explore_time[nxt] is None:
                    dfs(nxt, stack)
                    backedge[cur] = min(backedge[cur], backedge[nxt])
                if onstack[nxt]:
                    backedge[cur] = min(backedge[cur], explore_time[nxt])
            
            # print(f'{cur} After Loop {explore_time[cur]} == {backedge[cur]}')
            if explore_time[cur] == backedge[cur]:
                nonlocal scc
                if len(scc) > 1:
                    return
                scc = []
                # print(f'Cycle Found {cur} =>  {explore_time[cur], backedge[cur]}')
                while stack:
                    top = stack.pop()
                    onstack[top] = False
                    scc.append(top)
                    if top == cur:
                        break
                # print(scc)
            
        for cur in range(1, self.N+1):
            if explore_time[cur] is None:
                dfs(cur, [])
        
        scc = scc[::-1]
        cycle_edges = set()
        for frm, to in zip(scc, scc[1:]):
            cycle_edges.add(tuple([frm, to]))
        cycle_edges.add(tuple([scc[-1], scc[0]]))
        return cycle_edges

    
    def non_rooted_graph(self, g, edges):
        cycle_edges = self.find_cycle(g)
        # print()
        for a, b in reversed(edges):
            if tuple([a,b]) in cycle_edges:
                return [a, b]
        return [None, None]
        
        
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # If root found, try each edge and see if we can reach each nodes.
        # If no root found, that means root belongs to a cycle. Just remove the 
        # Last edge of the cycle.
        
        self.N, g = len(edges), defaultdict(list)
        root_candidate = set(range(1,self.N+1))
        
        for a, b in edges:
            g[a].append(b)
            root_candidate.discard(b)
        
        if len(root_candidate) == 1:
            return self.rooted_graph(root_candidate.pop(), g, edges)
        
        return self.non_rooted_graph(g, edges)
