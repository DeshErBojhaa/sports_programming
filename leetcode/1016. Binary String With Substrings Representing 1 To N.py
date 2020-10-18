# 1016. Binary String With Substrings Representing 1 To N
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        bl = N.bit_length()
        seen = set()
        S = list(map(int,S))
        
        for l in range(1, bl+1):
            cur = 0
            for i, v in enumerate(S):
                if i >= l:
                    cur -= S[i-l] * (1<< l)
                cur += v
                
                if 0 < cur <= N:
                    seen.add(cur)
                
                cur <<= 1
        # print(sorted(seen))
        return len(seen) == N
