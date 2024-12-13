class Solution:
    def findScore(self, nums: List[int]) -> int:
        h, sm = [(x, i) for i, x in enumerate(nums)], 0
        used = [False] * len(nums)
        heapify(h)

        while h:
            x, i = heappop(h)
            if used[i]:
                continue
            sm += x
            if i + 1 < len(nums):
                used[i + 1] = True
            if i - 1 > -1:
                used[i - 1] = True
            used[i] = True
        return sm
