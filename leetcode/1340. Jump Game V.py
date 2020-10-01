# 1340. Jump Game V
class Solution:
    def maxJumps(self, A: List[int], d: int) -> int:
        N = len(A)
        graph = defaultdict(list)
        
        def build(it):
            stack = []
            for i in it:
                while stack and A[stack[-1]] < A[i]:
                    j = stack.pop()
                    if abs(i-j) <= d:
                        graph[j].append(i)
                stack.append(i)
        
        build(range(N))
        build(reversed(range(N)))
        
        @lru_cache(None)
        def rec(i):
            return 1 + max(map(rec, graph[i]), default = 0)
        
        return max(map(rec, range(N)))
