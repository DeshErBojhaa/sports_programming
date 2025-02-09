from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        c = Counter(a-b for a,b in zip(nums, list(range(1, N+1))))
        print(c.keys(), c.values(), 'Bad', (((N) * (N-1)))//2)
        return (((N) * (N-1)))//2 - sum((x * (x-1))//2 for x in c.values())
    
    
