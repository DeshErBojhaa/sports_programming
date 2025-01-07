class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for a, b in product(words, words):
            if a == b:
                continue
            if b.find(a) > -1:
                ans.add(a)
        
        return ans
