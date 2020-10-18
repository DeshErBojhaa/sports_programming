# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        s = set(wordlist)
        while s:
            cur = s.pop()
            guess_val = master.guess(cur)
            if guess_val == 6:
                return
            
            ns = set()
            for now in s:
                match = sum(i==j for i,j in zip(cur, now))
                if match != guess_val:
                    ns.add(now)
            
            s -= ns
