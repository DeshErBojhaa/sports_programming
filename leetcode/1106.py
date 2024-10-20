class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        d = {'&': all, '|': any, '!': operator.not_}

        def get_parts(s):
            s = s[1:-1]
            tmp = ''
            parts, brace = [], 0
            for i, ch in enumerate(s):
                brace += (ch == '(')
                brace -= (ch == ')')
                
                if (ch == ',' and brace == 0):
                    parts.append(tmp.rstrip(','))
                    tmp = ''
                    continue
                tmp += ch
            if tmp:
                parts.append(tmp)
            if len(parts) == 1 and parts[0][-1] != ')':
                parts = parts[0].split(',')
                
            return parts
        
        def rec(s):
            if not s:
                return []
            if s == 't':
                return [True]
            if s == 'f':
                return [False]
            
            if s[0] in d:
                split = rec(s[1:])
                if s[0] == '!':
                    ans = not split.pop()
                else:
                    ans = d[s[0]](split)
                
                return [ans]
            
            if s[0] == '(':
                parts = get_parts(s)
                ans = []
                for p in parts:
                    ans.extend(rec(p))
                return ans
        
        ans = rec(expression)
        return ans.pop()
    
# "|(f,&(t,t))"
# "|(&(t,f,t),!(t))"
# "&(t,f)"
# "|(f,t)"
# "!(f)"
# "f"
# "t"
