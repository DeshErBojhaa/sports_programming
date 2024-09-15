class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        def generate(arr):
            d = defaultdict(lambda: -1)
            taken = {(0, 0)}
            for i, v in enumerate(arr):
                tmp_taken = set()
                for t, val in taken:
                    if t + 1 > k:
                        continue
                    val = val | v
                    tmp_taken.add((t + 1, val))
                    if val in d:
                        continue
                    if t + 1 == k:
                        d[val] = i + 1
                taken.update(tmp_taken)
            return d

        l = generate(nums)
        r = generate(nums[::-1])
        ans = 0
        for val_a, idx_a in l.items():
            for val_b, idx_b in r.items():
                if idx_a + idx_b > len(nums):
                    continue
                ans = max(ans, val_a ^ val_b)

        return ans
