class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        d = {}
        while N:
            d[tuple(cells)] = N
            N -= 1
            cells = [int(i > 0 and i < 7 and cells[i-1]==cells[i+1]) for i in range(8)]
            if tuple(cells) in d:
                N = N % (d[tuple(cells)] - N)
        return cells
