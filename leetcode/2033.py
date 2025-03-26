class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = sorted(itertools.chain.from_iterable(grid))
        mid = len(l) // 2
        cnt = 0
        for i in range(0, mid):
            c, d = divmod(l[mid] - l[i], x)
            if d:
                return -1
            cnt += c
        for i in range(mid + 1, len(l)):
            c, d = divmod(l[i] - l[mid], x)
            if d:
                return -1
            cnt += c
        return cnt
