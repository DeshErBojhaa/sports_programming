 def customSortString(self, S: str, T: str) -> str:
        c = Counter(T)
        ans = ''
        for s in S:
            ans += s*c[s]
            del c[s]
        
        for i, v in c.items():
            ans += i*v
        return ans
