class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        words = set(wordDict)
        
        def rec(rems):
            if rems in memo:
                return memo[rems]
            if not rems:
                return ['']
            
            ans = []
            for i in range(len(rems)+1):
                for w in words:
                    if rems[i:len(w)] == w:
                        rest = rec(rems[i+len(w):])
                        for rem in rest:
                            ans.append((w + ' ' + rem).strip())
            memo[rems] = ans
            return ans
        
        return rec(s)
