# 373. Find K Pairs with Smallest Sums
from heapq import heappush, heappop, heapify
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k:
            return []
        
        max_heap = []
        
        for i in range(min(len(nums2), k)):
            heappush(max_heap, (- (nums1[0] + nums2[i]), nums1[0], nums2[i]))
        

        for n1 in nums1[1:]:
            heap_updated = False
            for n2 in nums2:
                now = n1 + n2
                while len(max_heap) >= k and now < -max_heap[0][0]:
                    heappop(max_heap)
                
                if len(max_heap) < k:
                    heappush(max_heap, (-now, n1, n2))
                    heap_updated = True
                else:
                    break
            
            if not heap_updated:
                break
        
        ans = []
        while len(max_heap) > k:
            heappop(max_heap)

        while max_heap:
            _, n1, n2 = heappop(max_heap)
            ans.append((n1, n2))
        
        return ans
