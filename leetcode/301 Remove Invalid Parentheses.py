#301. Remove Invalid Parentheses
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        extra_l = extra_r = 0
        
        for c in s:
            if c == '(':
                extra_l += 1
            if c == ')':
                if extra_l > 0:
                    extra_l -= 1
                else:
                    extra_r += 1
        
        ans = []
        max_len = 0
        def rec(balance, cur, ext_l, ext_r, tmp):
            if balance < 0 or ext_l < 0 or ext_r < 0:
                return
            
            if cur == len(s):
                nonlocal max_len, ans
                if balance == 0:
                    if len(tmp) > max_len:
                        ans = [''.join(tmp)]
                        max_len = len(tmp)
                    elif len(tmp) == max_len:
                        ans.append(''.join(tmp))
                return
            
            if s[cur] not in '()':
                tmp.append(s[cur])
                rec(balance, cur+1, ext_l, ext_r, tmp)
                tmp.pop()
                return
            
            # Skip Part
            
            rec(balance, cur+1, ext_l - int(s[cur] == '('), ext_r - int(s[cur] == ')'), tmp)
            
            if s[cur] == '(':    
                tmp.append('(')
                rec(balance + 1, cur+1, ext_l, ext_r, tmp)
                tmp.pop()
            else:
                tmp.append(')')
                rec(balance - 1, cur+1, ext_l, ext_r, tmp)
                tmp.pop()
        
        rec(0, 0, extra_l, extra_r, [])
        
        anss = set()
        for v in ans:
            anss.add(v)
        
        
        return list(anss)
