# 1487. Making File Names Unique
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        cnt = collections.Counter()
        unique_names = set()
        ans = []
        
        for n in names:
            if n not in unique_names:
                unique_names.add(n)
                ans.append(n)
                continue
            
            for i in range(1, 1000000):
                nn = n + f'({i})'
                if nn in unique_names:
                    continue
                unique_names.add(nn)
                ans.append(nn)
                break
        
        return ans
        
        
