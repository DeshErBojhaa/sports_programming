class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot = 0
        N = len(nums)
        ss = sorted(nums)
        
        for i in range(N):
            nr = ss[i:] + ss[:i]
            # print('New', nr)
            
            if nr == nums:
                return True
        
        return False
