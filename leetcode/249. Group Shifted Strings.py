# 249. Group Shifted Strings
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        def calc(s):
            tup = None
            for i in range(1, len(s)):
                val = ord(s[i]) - ord(s[i-1])
                if val < 0:
                    val += 26
                if tup is None:
                    tup = (val,)
                else:
                    tup += (val,)
            return tup
        
        for s in strings:
            tup = calc(s)
            d[tup].append(s)
        
        return d.values()
