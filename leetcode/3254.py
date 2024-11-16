class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ans, last, cnt = [], -5425, 0
        for n in nums:
            if n != last + 1:
                cnt = 0
            last = n
            cnt += 1

            if cnt >= k:
                ans.append(last)
            else:
                ans.append(-1)

        return ans[k -1:]
