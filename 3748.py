class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        runs, starts, last = [1], [0], nums[0]
        for i, x in enumerate(nums[1:], 1):
            if x >= last:
                runs.append(runs[-1] + 1)
            else:
                runs.append(1)
                starts.append(i)
            last = x
        acc_runs = list(accumulate(runs))
        ans = []
        # print('starts', starts)
        # print('acc_runs', acc_runs)

        for a, b in queries:
            if a == b:
                ans.append(1)
                continue
            
            l_idx = bisect_left(starts, a)
            if l_idx >= len(starts):
                l = a
            else:
                l = starts[l_idx]
            if l > b:
                l = a
            l_len = max(0, l - a)
            l_cnt = (l_len * (l_len + 1)) // 2

            r_idx = bisect_left(starts, b)
            if r_idx >= len(starts) or starts[r_idx] > b:
                r_idx -= 1
            r = starts[r_idx]
            r_len = max(0, b - r + 1)
            r_cnt = (r_len * (r_len + 1)) // 2

            mid = 0
            if r > l:
                mid = acc_runs[r - 1] - (acc_runs[l-1] if l else 0)
            if l_idx > r_idx:
                l = a
                l_len = 0
                l_cnt = 0
                r = b
                r_len = 0
                r_cnt = 0
                ln = b - a + 1
                mid = (ln * (ln + 1)) // 2

            ans.append(l_cnt + mid + r_cnt)
            # print('a:', a, 'b:', b)
            # print('l_idx', l_idx, 'l', l, 'l_len', l_len, 'l_cnt', l_cnt)
            # print('r_idx', r_idx, 'r', r, 'r_len', r_len, 'r_cnt', r_cnt)
            # print('mid', mid, 'ans', ans[-1])
        return ans
