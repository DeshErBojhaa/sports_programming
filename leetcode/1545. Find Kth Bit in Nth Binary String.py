# 1545. Find Kth Bit in Nth Binary String
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def build(s):
            tmp = ['1' if x == '0' else '0' for x in s]
            return s + '1' + ''.join(tmp[::-1])
        s = '0'
        
        while len(s) < k:
            s = build(s)
        
        return s[k-1]
