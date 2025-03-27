class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = Counter(nums)
        x = c.most_common(1)[0][0]
        freq = list(accumulate([int(v == x) for v in nums]))
        
        for i in range(0, len(nums) - 1):
            l_len = i + 1
            l_cnt = freq[i]

            if l_cnt * 2 <= l_len:
                continue
            
            r_len = len(nums) - i - 1
            r_cnt = freq[-1] - l_cnt

            if r_cnt * 2 <= r_len:
                continue
            
            return i
        return -1

        return -1
