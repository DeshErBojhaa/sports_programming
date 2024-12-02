class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, v in enumerate(sentence.split()):
            if v.startswith(searchWord):
                return i + 1
        
        return -1
