# 212. Word Search II
from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.word = True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        R, C = len(board), len(board[0])
        if not R or not C:
            return []
        
        trie = Trie()
        
        for w in words:
            trie.insert(w)
        
        ans = []
        def backtrack(i, j, node, word=''):
            # print(i, j, word)
            if node.word:
                node.word = False
                ans.append(word)
                
            if i < 0 or i >= R or j < 0 or j >= C or board[i][j] == '#':
                return
            
            ch = board[i][j]
            node = node.children.get(ch, None)
            if node is None:
                return
            
            board[i][j] = '#'
            
            backtrack(i+1, j, node, word+ch)
            backtrack(i-1, j, node, word+ch)
            backtrack(i, j+1, node, word+ch)
            backtrack(i, j-1, node, word+ch)
            
            board[i][j] = ch
        
        for i in range(R):
            for j in range(C):
                backtrack(i, j, trie.root)
                
        return ans
