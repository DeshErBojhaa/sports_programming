#378. Kth Smallest Element in a Sorted Matrix
from queue import PriorityQueue
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        d = {i:0 for i in range(len(matrix))}
        
        pq = PriorityQueue()
        
        for i, v in enumerate(matrix):
            pq.put((v[0], i))
        
        n = 0;
        cur = None
        while n < k:
            cur, i = pq.get()
            if d[i] < len(matrix[i]) - 1:
                d[i] = d[i] + 1
                pq.put((matrix[i][d[i]], i))
            n += 1
        return cur
