# 785. Is Graph Bipartite?
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        nodes = set()
        
        def dfs(cur, cur_color):
            if cur in color:
                return cur_color == color[cur]
            
            nodes.add(cur)
            color[cur] = cur_color
            ans = True
            for nxt in graph[cur]:
                ans &= dfs(nxt, 1 - cur_color)
            
            return ans
        
        is_bip = True
        for i, v in enumerate(graph):
            if not v or i in color:
                continue
            is_bip &= dfs(i, 0)

        return is_bip
