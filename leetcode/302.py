from ast import main
from math import inf
from typing import List

def minArea(image: List[List[str]], x: int, y: int) -> int:
    l, r, u, d = inf, -1, inf, -1

    for i, row in enumerate(image):
        for j, c in enumerate(row):
            if c == '0':
                continue
            l = min(l, j)
            r = max(r, j)

            u = min(u, i)
            d = max(d, i)
    print(l, r, u, d)
    return (r - l + 1) * (d - u + 1)


def test_1():
    ans = minArea(image=[["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x=0, y=2)
    assert ans == 6


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])