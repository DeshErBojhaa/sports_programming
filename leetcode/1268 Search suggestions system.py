from collections import OrderedDict
chars = 'abcdefghijklmnopqrstuvwxyz'

class Node:
    def __init__(self):
        self.d = OrderedDict((k, None) for k in chars)
        self.end = None

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        def build_trie(par, ind, w):
            if ind == len(w):
                return
            ch = w[ind]
            nd = par.d[ch]
            
            if not nd:
                nd = Node()
            par.d[ch] = nd
            
            if ind == len(w) - 1:
                nd.end = w
            build_trie(nd, ind+1, w)
            
        def trav_trie(ind, pref, cur, ans):
            if len(ans) >= 3:
                return
            if not cur:
                return
            if cur.end and ind>=len(pref) and len(ans) < 3:
                ans.append(cur.end)
            if ind < len(pref):
                ch = pref[ind]
                trav_trie(ind+1, pref, cur.d[ch], ans)
                return
            for k, v in cur.d.items():
                if not v:
                    continue
                if len(ans) >= 3:
                    return
                trav_trie(ind, pref, v, ans)
        
        root = Node()
        for p in products:
            build_trie(root, 0, p)
        
        rett = []
        for i, c in enumerate(searchWord):
            a = []
            trav_trie(0, searchWord[:i+1], root, a)
            rett.append(a)
        return rett
