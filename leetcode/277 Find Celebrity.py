# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from functools import lru_cache
class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb_candidate = 0
        
        @lru_cache(maxsize=None)
        def _knows(i, j):
            return knows(i, j)
        
        for i in range(1, n):
            if _knows(celeb_candidate, i):
                celeb_candidate = i
        
        for i in range(n):
            if i == celeb_candidate:
                continue
            if not _knows(i, celeb_candidate) or _knows(celeb_candidate, i):
                return -1
        return celeb_candidate
