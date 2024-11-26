class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = defaultdict(int)
        for a,b in edges:
            indeg[b] = indeg[b] + 1
        
        cnt = 0
        ans = -1
        for i in range(n):
            if indeg[i] == 0:
                cnt = cnt + 1
                ans = i
        return ans if cnt == 1 else -1
