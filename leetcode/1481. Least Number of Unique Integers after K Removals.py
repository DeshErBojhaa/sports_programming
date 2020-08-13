# 1481. Least Number of Unique Integers after K Removals
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        
        for n, v in sorted(c.items(), key=lambda x: x[1]):
            mn = min(k, c[n])
            c[n] -= mn
            k -= mn
            
            if not k:
                break
        
        return sum(v > 0 for v in c.values())
