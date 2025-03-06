class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        al = set(range(1, (n*n) + 1))
        seen, dup = set(), None

        for li in grid:
            for x in li:
                if x in seen:
                    dup = x
                    continue
                seen.add(x)
                al.remove(x)
        return [dup, al.pop()]
