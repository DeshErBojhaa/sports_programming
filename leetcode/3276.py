class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        nums = defaultdict(set)
        for i, g in enumerate(grid):
            for v in g:
                nums[v].add(i)
        nums = list(nums.items())

        @cache
        def rec(cur, mask):
            if cur == len(nums) or mask == 0:
                return 0
            
            ret = rec(cur + 1, mask)
            for row in nums[cur][1]:
                if mask & (1<<row) == 0:
                    continue
                nm = mask ^ (1 << row)
                ret = max(ret, rec(cur+1, nm) + nums[cur][0])
            
            return ret
        
        return rec(0, (1<<len(grid))-1)
