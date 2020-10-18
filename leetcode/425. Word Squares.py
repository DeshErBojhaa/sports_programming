# 425. Word Squares
class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.end = False
        
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans, N, M = [], len(words), len(words[0])
        
        root = Node()
        
        # Insert all words in trie
        for w in words:
            cur = root
            for ch in w:
                cur = cur.child[ch]
            cur.end = True
        
        def get_all(cur, st, ans):
            if cur.end:
                ans.append(st)
                return
            for ch, nxt in cur.child.items():
                get_all(nxt, st + ch, ans)
        
        def pref_match(st):
            cur = root
            for ch in st:
                if ch not in cur.child:
                    return []
                cur = cur.child[ch]
            ans = []
            get_all(cur, st, ans)
            return ans
        

        def rec(square):
            # print(square)
            if len(square) == M:
                ans.append(square)
                return
            
            idx = len(square)
            pref = []
            
            for r in range(idx):
                pref.append(square[r][idx])
            
            for nxt in pref_match(''.join(pref)):
                rec(square + [nxt])
        
        for w in words:
            rec([w])
        return ans
 
