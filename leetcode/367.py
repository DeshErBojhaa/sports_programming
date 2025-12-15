class Solution:
    def maxPoints(self, t: List[int], tt: List[int], k: int) -> int:
        N = len(t)
        rem, seen = N - k, [False] *  N
        heap, taken, ans = [], 0, 0

        for i, (a, b) in enumerate(zip(t, tt)):
            heappush(heap, [b - a,i])
        
        while k:
            _, idx = heappop(heap)
            ans += t[idx]
            seen[idx] = True
            k -= 1
        
        return ans + sum(max(x,y) for i, (x, y) in enumerate(zip(t, tt)) if not seen[i])
