    def scoreOfParentheses(self, S: str) -> int:
        ans = []
        for s in S:
            if s == '(':
                ans.append('(')
                continue
            
            val = 0
            while ans[-1] != '(':
                val += int(ans.pop())
            
            ans.pop()
            if val == 0:
                ans.append(1)
            else:
                ans.append(val * 2)
        
        #print(ans)
        return sum(ans)
