from typing import List
from collections import deque

def minArea(image: List[List[str]], x: int, y: int) -> int:
    l, r, u, d = y, y, x, x
    image[x][y] = '0'
    R, C = len(image), len(image[0])

    q = deque([(x, y)])
    while q:
        row, col = q.popleft()
        l, r = min(l, col), max(r, col)
        u, d = min(u, row), max(d, row)
        for nr, nc in [(row, col+1), (row+1, col), (row, col-1), (row-1, col)]:
            if not 0 <= nr < R or not 0 <= nc < C:
                continue
            if image[nr][nc] == '0':
                continue
            image[nr][nc] = '0'
            q.append((nr, nc))

    return (r - l + 1) * (d - u + 1)


def test_1():
    ans = minArea(image=[["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x=0, y=2)
    assert ans == 6


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])