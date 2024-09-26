class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        N, sorted_nums = len(nums), sorted(nums)
        ans, bit = 0, [0] * (N + 1)

        def query(i):
            i += 1
            ans = 0
            while i <= N:
                ans += bit[i]
                i += i&-i
            return ans

        def update(i):
            i += 1
            while i > 0:
                bit[i] += 1
                i -= (i & -i)


        for n in nums:
            idx = bisect_left(sorted_nums, n * 2 + 1)
            aa = query(idx)
            ans += aa
            idx = bisect_left(sorted_nums, n)
            update(idx)
        
        return ans
