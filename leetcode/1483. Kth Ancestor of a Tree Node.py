# 1483. Kth Ancestor of a Tree Node
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.depth, self.par = [0]*n, [None]*n
        self.g = collections.defaultdict(list)
        
        for i, v in enumerate(parent):
            self.par[i] = v
            self.g[v].append(i)
        
        def dfs(cur, dep = 0):
            self.depth[cur] = dep
            for nxt in self.g[cur]:
                dfs(nxt, dep + 1)
        
        dfs(0)
        max_depth = max(self.depth)
        if max_depth == 0:
            self.dp = None
            return
        
        self.lg = math.ceil(math.log2(max_depth))
        
        self.dp = [[None] * (self.lg+1) for _ in range(n)]
        
        for i in range(n):
            self.dp[i][0] = parent[i]
        
        for k in range(1, self.lg+1):
            for i in range(n):
                mid = self.dp[i][k-1]
                if mid is None or mid < 0:
                    continue
                self.dp[i][k] = self.dp[mid][k-1]
        
    
    def getKthAncestor(self, node: int, k: int) -> int:
        now = node
        if not self.dp:
            return -1
        for i in range(self.lg, -1, -1):
            if k >= (2**i):
                k -= (2**i)
                if self.dp[now][i] is not None and self.dp[now][i] > -1:
                    now = self.dp[now][i]
                else:
                    return -1
    
        return now


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
