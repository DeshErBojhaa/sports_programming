import bisect
class Solution:
    def medianSlidingWindow(self, n: List[int], k: int) -> List[float]:
        if not n:
            return []
        median = []
        sorted_k = sorted(n[:k])
        
        for i, x in enumerate(n):
            right_to_mid = k//2
            left_to_mid = ~(k//2)
            median.append((sorted_k[right_to_mid]+sorted_k[left_to_mid])/2.)
            sorted_k.remove(x)
            if i+k >= len(n):
                break
            bisect.insort(sorted_k, n[i+k])
        return median
