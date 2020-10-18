def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = sorted(deck)[::-1]
        ans = [0] * len(d)
        
        idx = 0
        skipped = True
        
        while d:
            if ans[idx] == 0:
                if skipped:
                    ans[idx] = d.pop()
                    skipped = False
                else:
                    skipped = True
            
            idx = (idx + 1)%len(deck)
            
        return ans
