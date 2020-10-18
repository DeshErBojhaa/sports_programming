class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        relation = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        N = len(digits)
        ans = []
        
        def rec(ind, s):
            if ind == N:
                ans.append(s)
                return
            
            for c in relation[digits[ind]]:
                rec(ind+1, s + c)
        
        rec(0, '')
        return ans
