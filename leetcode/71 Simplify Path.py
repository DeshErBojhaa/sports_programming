# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path
        p = path.split('/')
        ans = []
        for v in p:
            if v == '..':
                if ans:
                    ans.pop()
            elif v == '.' or not v:
                continue
            else:
                ans.append(v)
        
        return '/' + '/'.join(ans)
