# 609. Find Duplicate File in System
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for p in paths:
            path, *name_and_content = p.split()
            for nac in name_and_content:
                name, content = nac.split('(')
                d[content].append('/'.join([path,name]))
        
        return [v for v in d.values() if len(v) > 1]
