from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ''

        c = Counter(S)
        ans = []
        
        while len(c) > 1:
            c1, c2 = c.most_common(2)
            if ans and c1[0] == ans[-1]:
                ans.extend([c2[0], c1[0]])
            else:
                ans.extend([c1[0], c2[0]])
            
            c[c1[0]] -= 1
            c[c2[0]] -= 1
            
            if c[c1[0]] == 0:
                del c[c1[0]]
            if c[c2[0]] == 0:
                del c[c2[0]]
        
        if len(c) == 1:
            c1 = c.most_common(1)[0]
            if c1[1] > 1:
                return ""
            ans.append(c1[0])
        
        return ''.join(ans)
