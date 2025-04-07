class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N, sm = len(nums), sum(nums)
        if sm % 2:
            return False
        
        @lru_cache(None)
        def rec(cur, rem):
            if rem <= 0:
                return rem == 0
            if cur == N:
                return False
            
            return rec(cur+1, rem) or rec(cur+1, rem - nums[cur])
        
        return rec(0, sm // 2)
