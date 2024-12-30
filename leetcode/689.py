class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        nums = list(accumulate(nums))
        print(nums)
        N = len(nums)
        nums += [0]

        @cache
        def rec(cur, tkn):
            if tkn == 3:
                return 0
            if cur + k > N:
                return -inf
            
            # take
            take = nums[cur + k - 1] - nums[cur - 1]
            ans = rec(cur + k, tkn + 1) + take
            ans = max(ans, rec(cur + 1, tkn))

            return ans

        max_sm = rec(0, 0)
        p = []
        def path(cur, tkn, sm):
            if cur == N or tkn == 3:
                return
            take = nums[cur + k - 1] - nums[cur - 1]
            if rec(cur + k, tkn + 1) == sm - take:
                p.append(cur)
                path(cur + k, tkn + 1, sm - take)
                return
            path(cur + 1, tkn, sm)

        path(0, 0, max_sm)

        return p
