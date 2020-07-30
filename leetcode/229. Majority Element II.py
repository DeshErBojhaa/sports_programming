# 229. Majority Element II
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter()
        N = len(nums)
        
        for n in nums:
            c[n] += 1
            if len(c) == 3:
                c -= Counter(c.keys())
            
        return [n for n in c if nums.count(n) > N//3]
