class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = sorted(nums)
        min_dist = float('inf')
        ans = -1
        # Find x <= y<= z
        for i, x in enumerate(n[:-2]):
            rem = target - x
            lo, hi = i+1, len(n)-1
            
            while lo < hi:
                y = n[lo]
                z = n[hi]
                sm = x + y + z
                if abs(target - sm) < min_dist:
                    min_dist = abs(target - sm)
                    ans = sm
                
                if sm > target:
                    hi -= 1
                else:
                    lo += 1
        return ans
