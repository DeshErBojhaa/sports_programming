# 1032. Stream of Characters
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.end = False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = []
        self.root = Node()
        for w in words:
            cur = self.root
            for ch in reversed(w):
                cur = cur.children[ch]
            cur.end = True
        

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        cur = self.root
        
        for ch in reversed(self.letters):
            # print(ch, cur.children.keys())
            if cur.end:
                return True
            if ch not in cur.children:
                # print('Returning False', ch, cur.children.keys())
                return False
            cur = cur.children[ch]
        
        return cur.end


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
