class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        dec, inc = [1] * N, [1] * N
        
        for i, v in enumerate(nums[1:], 1):
            if v > nums[i-1]:
                continue
            dec[i] += dec[i-1]
        
        for i in range(N-2, -1, -1):
            if nums[i] > nums[i+1]:
                continue
            inc[i] += inc[i+1]
        
        x = []
        for i in range(1, N-1):
            if dec[i-1] >= k and inc[i+1] >= k:
                x.append(i)
        return x