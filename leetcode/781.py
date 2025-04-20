class Solution:
    def numRabbits(self, aa: List[int]) -> int:
        c = Counter(aa)
        return sum(ceil(v / (k+1)) * (k + 1) for k, v in c.items())
