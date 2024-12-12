class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g = [-n for n in gifts]
        heapify(g)
        for _ in range(k):
            x = -heappop(g)
            x = floor(sqrt(x))
            heappush(g, -x)
        return -sum(g)
