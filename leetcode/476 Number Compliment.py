from math import log2
class Solution:
    def findComplement(self, num: int) -> int:
        lg = int(log2(num)) + 1
        
        for i in range(lg):
            num = num ^ (1<<i)
        return num
