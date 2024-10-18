class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = reduce(lambda a,b: a | b, nums)
        N = len(nums)

        @cache
        def rec(cur, sm):
            if sm > target:
                return 0
            if cur == N:
                return int(sm == target)
                
            return rec(cur+1, sm) + rec(cur+1, sm | nums[cur])

        return rec(0, 0)
