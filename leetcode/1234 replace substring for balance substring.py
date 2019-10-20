def ok(nc, c):
    return all(nc[ch] >= v for ch, v in c.items())

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)//4
        c = Counter(s)
        
        for ch in 'QWER':
            if ch not in c:
                continue
            if c[ch] > n:
                c[ch] = c[ch] - n
            else:
                c.pop(ch)
        
        if not c:
            return 0
        lo, hi, ans = 0, 0, n*4
        nc = Counter(s[0])
        
        while lo<= hi and hi < n*4:
            if not ok(nc, c):
                hi += 1
                if hi < n*4:
                    nc.update(s[hi])
                continue
            
            nc.subtract(s[lo])
            ans = min(ans, hi - lo + 1)
            lo += 1
        return ans
    
# "QQWE"
# "QQQQ"
# "QWER"
# "WWWRRRER"
# "WWQQRRRRQRQQ"
# "WWEQERQWQWWRWWERQWEQ"
# "WQWRQQQW"
