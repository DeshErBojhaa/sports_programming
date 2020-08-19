# 642. Design Search Autocomplete System
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.endhere = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.cur_query = ''
        self.root = Node()
        
        for s, h in zip(sentences, times):
            self.inserttrie(s, h)
        
        
    def inserttrie(self, s, hotness=0):
        cur = self.root
        for c in s:
            cur = cur.children[c]
        
        cur.endhere += max(1, hotness)
    
    
    def search(self, s):
        cur = self.root
        string = ''
        for c in s:
            cur = cur.children[c]
            string += c
        
        return self.get_all(cur, string)
        
    
    def get_all(self, cur, string):
        if not cur.children:
            if cur.endhere:
                return [[cur.endhere, string]]
            return []
        ans = []
        if cur.endhere:
            ans.extend([[cur.endhere, string]])
            
        for ch, nxt in cur.children.items():
            tmp = self.get_all(nxt, string+ch)
            if tmp:
                ans.extend(tmp)
        return ans
    
        
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.inserttrie(self.cur_query)
            self.cur_query = ''
            return
        self.cur_query += c
        res = self.search(self.cur_query)
        # print(res)
        return (x[1] for x in sorted(res, key=lambda l: (-l[0], l[1]))[:3])


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# ["AutocompleteSystem","input","input","input","input"]
# [[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"]]
