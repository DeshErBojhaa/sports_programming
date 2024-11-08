class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        tot, max_num = 0, 2**maximumBit
        for v in nums:
            tot ^= v
        
        def find(a, b):
            return a ^ b
        
        ans = []
        for v in nums[::-1]:
            ans.append(find(tot, max_num - 1))
            tot ^= v
        
        return ans
