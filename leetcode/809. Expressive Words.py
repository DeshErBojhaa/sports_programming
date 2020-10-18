# 809. Expressive Words
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        ans = 0 
        
        def is_expressive(w):
            si, wi = 0, 0
            while si < len(S) and wi < len(w):
                if S[si] != w[wi]:
                    return 0
                s_count, w_count = 0, 0
                s_char, w_char = S[si], w[wi]
                while si < len(S) and S[si] == s_char:
                    si += 1
                    s_count += 1
                while wi < len(w) and w[wi] == w_char:
                    wi += 1
                    w_count += 1
                diff = s_count - w_count

                if diff < 0:
                    return 0
                if diff == 0:
                    continue
                if diff + w_count < 3:
                    return 0

            return int(si == len(S) and wi == len(w) )
            
            
        for w in words:
            ans += is_expressive(w)
        
        return ans

