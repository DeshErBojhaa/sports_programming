# 898. Bitwise ORs of Subarrays
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        s = set()
        global_set = set()

        for v in A:
            s = {x|v for x in s} | {v}
            global_set |= s
            
        return len(global_set)
