# 179. Largest Number
class Cmp(str):
    def __lt__(x,y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ret = ''.join(sorted(map(str, nums), key=Cmp))
        return '0' if ret[0] == '0' else ret

# [824,1399,5607,6973,5703,4398]
# 9609 938 8247
# 9609 938 824 8247 6973 5703 5607 4398 1399
