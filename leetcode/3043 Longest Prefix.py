class Node:
    def __init__(self):
        self.word = False
        self.children = [None] * 10

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, s):
        cur = self.root
        for nm in s:
            if cur.children[nm] == None:
                cur.children[nm] = Node()
            cur = cur.children[nm]
        cur.word = True
    
    def search(self, s):
        cur = self.root
        for i, nm in enumerate(s):
            if cur.children[nm] == None:
                return i
            cur = cur.children[nm]
        return len(s)

class Solution:
    def longestCommonPrefix(self, aa: List[int], bb: List[int]) -> int:
        aa, bb = list(map(str, aa)), list(map(str, bb))
        tt = Trie()
        for b in bb:
            b = list(map(int, b))
            tt.insert(b)
        ans = 0
        for a in aa:
            a = list(map(int, a))
            ans = max(ans, tt.search(a))
        return ans
