# 211 Add and Search Word - Data structure design
from collections import defaultdict

class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.word_end = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for i, w in enumerate(word):
            cur = cur.next[w]
        cur.word_end = True  
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def _search(ind, cur):
            if ind == len(word):
                return cur.word_end
            
            if word[ind] == '.':
                return any(_search(ind+1, nxt) for nxt in cur.next.values())
            if word[ind] not in cur.next:
                return False
            return _search(ind+1, cur.next[word[ind]])
        
        return _search(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
