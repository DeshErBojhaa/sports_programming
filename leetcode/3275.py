class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        q = list(map(lambda a: abs(a[0]) + abs(a[1]), queries))

        ans = []
        for v in q:
            heappush(heap, -v)
            while len(heap) > k:
                heappop(heap)
            
            ans.append(-1 if len(heap) < k else -heap[0])
        
        return ans
