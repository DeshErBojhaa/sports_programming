# 1100 Find K-Length Substrings With No Repeated Characters
from collections import Counter
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if not S or not K or len(S) < K:
            return 0
        
        window = Counter(S[:K])
        ans = int(len(window) == K)
        
        for i in range(K, len(S)):
            window[S[i-K]] -= 1
            window[S[i]] += 1
            
            if window[S[i-K]] == 0:
                del window[S[i-K]]

            ans += int(len(window) == K)
        return ans
        
        
