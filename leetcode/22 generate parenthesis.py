def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def make(l, r, s):
            if not l and not r:
                ans.append(s)
                return
            if l < 0 or r < 0:
                return
            if l > r:
                return
            
            make(l-1, r, s+'(')
            make(l, r-1, s+')')
        
        make(n, n, '')
        return ans
