from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bool = Counter()
        for i,j in zip(secret, guess):
            if i == j:
                bool[i] += 1
        sc = Counter(secret)
        gc = Counter(guess)
        
        cow, bull = 0, sum(bool.values())
        for num, freq in sc.items():
            if num not in gc:
                continue
            cow += max(0, min(freq, gc[num]) - bool[num])
        
        ans = str(bull)+'A'+str(cow)+'B'
        
        return ans
