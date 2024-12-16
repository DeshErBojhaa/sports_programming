class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        a = [[x, i] for i, x in enumerate(nums)]
        heapify(a)

        for _ in range(k):
            x = heappop(a)
            x[0] *= multiplier
            heappush(a, x)
        
        ans = []
        for x in sorted(a, key=lambda z: z[1]):
            ans.append(x[0])
        return ans
