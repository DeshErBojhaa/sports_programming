class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * (n-1) * (n-1) + (n * 2 - 1)
