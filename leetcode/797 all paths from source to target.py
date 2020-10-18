 def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, n = [], len(graph)
        def trav(cur, path):
            if cur == n-1:
                ans.append(path[:])
                return
            for nxt in graph[cur]:
                path.append(nxt)
                trav(nxt, path)
                path.pop()
            
        trav(0, [0])
        return ans
