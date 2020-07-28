# 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {v:i for i, v in enumerate(order)}
        
        def lexico(a, b):
            for c1, c2 in zip(a, b):
                if pos[c1] < pos[c2]:
                    return True
                elif pos[c1] > pos[c2]:
                    return False
                
            return len(a) <= len(b)
        
        for i, v in enumerate(words):
            for w in words[i+1:]:
                if not lexico(v, w):
                    return False
        
        return True
