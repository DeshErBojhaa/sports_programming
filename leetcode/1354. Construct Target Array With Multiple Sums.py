# 1354. Construct Target Array With Multiple Sums
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        N = len(target)
        if N == 1:
            return target[0] == 1
        if N == 2 and (target[0] == 1 or target[1] == 1):
            return True
        
        max_q = [-x for x in target]
        heapify(max_q)
        sm = sum(target)
        
        while -max_q[0] > 1:
            largest = -max_q[0]
            rest = sm - largest
            
            if rest == 1:
                return True
            x = largest%rest
            
            # print(largest, '->', x, rest)
            
            if x == 0 or x == largest:
                return False
            
            sm = sm - largest + x
            heapreplace(max_q, -x)
        
        return True
