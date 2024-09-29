class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        def ok(s):
            if len(s) < 5 + k:
                return False
            v = set('aeiou')
            vv = set('aeiou')
            cons = 0
            for ch in s:
                if ch not in vv:
                    cons += 1
                    continue
                if ch in v:
                    v.remove(ch)
            return len(v) == 0 and cons == k
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                ans += ok(word[i:j])
        return ans
