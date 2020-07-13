# 1282. Group the People Given the Group Size They Belong To
from collections import defaultdict
class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        g = defaultdict(list)
        
        for i, v in enumerate(gs):
            g[v].append(i)
        
        ans = []
        
        for k in g:
            cnt, tmp_list = 0, []
            for x in g[k]:
                tmp_list.append(x)
                cnt += 1
                
                if cnt == k:
                    cnt = 0
                    ans.append(list(tmp_list))
                    tmp_list = []
        
        return ans
