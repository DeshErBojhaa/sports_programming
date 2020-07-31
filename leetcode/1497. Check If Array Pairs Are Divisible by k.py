# 1497. Check If Array Pairs Are Divisible by k
from collections import Counter
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modcount = Counter([x%k for x in arr])
        
        # 0 mod is not even
        if modcount[0]%2:
            return False
        
        for mod, cnt in modcount.items():
            if mod == 0:
                continue

            req = k - mod
            if cnt != modcount[req]:
                return False
        
        return True
        
