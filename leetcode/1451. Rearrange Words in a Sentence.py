# 1451. Rearrange Words in a Sentence
class Solution:
    def arrangeWords(self, text: str) -> str:
        if not text:
            return text
        
        l = sorted([(len(w),i,w) for i, w in enumerate(text.split())])
        
        return ' '.join([v[2] for v in l]).capitalize()
        
        
