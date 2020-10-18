# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [a-b for a, b in zip(gas, cost)]
        lis, lis_end, lis_max = 0, 0, 0
        if sum(diff) < 0:
            return -1
        
        for i in range(len(diff)):
            if lis + diff[i] < 0:
                lis = 0
            
            if lis + diff[i] > 0:
                if lis + diff[i] > lis:
                    lis_end = i
                    lis_max = lis + diff[i]
                lis = lis + diff[i]
        
        st = -1
        for i in range(lis_end, -1, -1):
            st = i
            lis_max -= diff[i]
            if lis_max <= 0:
                break
        
        return st
            
