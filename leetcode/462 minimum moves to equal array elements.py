def minMoves2(self, nums: List[int]) -> int:
        n = sorted(nums)
        return sum(abs(i - n[len(n)//2]) for i in n)
