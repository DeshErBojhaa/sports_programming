# 567. Permutation in String
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needle, haystack = Counter(s1), Counter()
        
        start, end = 0, 0
        
        while end < len(s2):
            if s2[end] not in needle:
                haystack.clear()
                start = end + 1
            else:
                haystack[s2[end]] += 1
                if needle == haystack:
                    return True
                while haystack[s2[end]] > needle[s2[end]]:
                    haystack[s2[start]] -= 1
                    start += 1
    
            end += 1
        
        return False
