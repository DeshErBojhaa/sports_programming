from collections import defaultdict
class Node:
    def __init__(self):
        self.next= defaultdict(Node)
        self.word_end = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word:
            next = cur.next[w]
            cur = next
        cur.word_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for w in word:
            if w not in cur.next:
                return False
            cur = cur.next[w]
        return cur.word_end
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for w in prefix:
            if w not in cur.next:
                return False
            cur = cur.next[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
