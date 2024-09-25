class Node:
    def __init__(self):
        self.child = [None] * 26
        self.cnt = 0
        self.leaf = False


aaa = ord('a')


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, ss):
        now = self.root
        for s in ss:
            idx = ord(s) - aaa
            if not now.child[idx]:
                now.child[idx] = Node()
            now = now.child[idx]
            now.cnt += 1

        now.leaf = True

    def search(self, ss):
        now, cnt = self.root, 0
        for s in ss:
            index = ord(s) - aaa
            now = now.child[index]
            cnt += now.cnt
        return cnt

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        t = Trie()
        for w in words:
            t.insert(w)
        
        for w in words:
            ans.append(t.search(w))
        
        return ans
