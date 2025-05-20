class Solution:
    def isZeroArray(self, nums: List[int], qq: List[List[int]]) -> bool:
        N = len(nums)
        arr = [0] * (N + 1)

        for a, b in qq:
            arr[a] += 1
            arr[b+1] -= 1
        
        arr = list(accumulate(arr))

        return all(a >= b for a, b in zip(arr, nums))
