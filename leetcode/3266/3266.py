def pow_times(a, b, m):
    cnt = 0
    while a < b:
        a *= m
        cnt += 1
    return max(1, cnt)
    
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        MOD = (10**9) + 7
        if len(nums) == 1:
            return [(nums[0] * pow(multiplier, k, MOD))%MOD]

        seen, rem_loop = set(), k
        num_order = [(v,i) for i, v in enumerate(nums)]
        heapq.heapify(num_order)

        while rem_loop:
            if len(seen) == len(nums):
                break
            v, idx = heapq.heappop(num_order)
            if idx in seen:
                seen = set()

            times = pow_times(v, num_order[0][0], multiplier)
            times = min(times, rem_loop)

            heapq.heappush(num_order, ((v * (multiplier ** times)), idx))
            seen.add(idx)
            rem_loop -= times

        t, d = divmod(rem_loop, len(nums))
        while num_order:
            v, idx = heapq.heappop(num_order)
            nums[idx] = v * pow(multiplier, t, MOD)
            if d:
                nums[idx] *= multiplier
                d -= 1
            nums[idx] %= MOD

        return nums
