# 1320. Minimum Distance to Type a Word Using Two Fingers
class Solution:
    def minimumDistance(self, word: str) -> int:
        N = len(word)
        word = [*map(lambda x: ord(x) - ord('A'), word)]
        
        def distance(n1, n2):
            a, b = divmod(n1, 6)
            a2, b2 = divmod(n2, 6)
            
            return abs(a2-a) + abs(b2- b)
        
        
        @lru_cache(None)
        def rec(a, b, idx):
            if idx == N:
                return 0
            
            ans = math.inf
            
            # Move first finger to cur location
            cost = 0
            if a is not None:
                cost = distance(a, word[idx])
            ans = min(ans, rec(word[idx], b, idx+1) + cost)
            
            cost = 0
            if b is not None:
                cost = distance(b, word[idx])
            ans = min(ans, rec(a, word[idx], idx+1) + cost)
            
            return ans
        
        return rec(None, None, 0)
