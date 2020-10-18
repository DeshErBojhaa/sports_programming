# 1554. Strings Differ by One Character
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        if not dict or not dict[0]:
            return False
        N, M = len(dict), len(dict[0])
        hash_, mod = [0] * N, (10**9) + 7
        
        for i in range(N):
            for j in range(M):
                hash_[i] = (hash_[i] * 26 + ord(dict[i][j]) - ord('a')) % mod
        
        def check(a, b):
            diff = 0
            for ch1, ch2 in zip(a, b):
                diff += int(ch1 != ch2)
            return diff == 1
        
        pos_pow = 1
        for j in range(M-1,-1,-1):
            seen = {}
            for i in range(N):
                skip_char_hash = hash_[i] - (pos_pow * (ord(dict[i][j]) - ord('a')))
                skip_char_hash %= mod
                
                if skip_char_hash in seen and check(dict[i], seen[skip_char_hash]):
                    return True
                seen[skip_char_hash] = dict[i]
            
            pos_pow *= 26
            pos_pow %= mod
        
        return False
