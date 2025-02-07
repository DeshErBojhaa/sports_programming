class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ctb, btc = defaultdict(set), defaultdict(lambda: -1)
        ans = []

        for b, c in queries:
            existing_col = btc[b] 
            if existing_col != -1:
                ctb[existing_col].remove(b)
                if len(ctb[existing_col]) == 0:
                    del ctb[existing_col]
            ctb[c].add(b)
            btc[b] = c
            ans.append(len(ctb))
        
        return ans
