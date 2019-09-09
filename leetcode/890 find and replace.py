def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            ok = True
            if len(word) != len(pattern):
                continue
            d, _d = {}, {}
            for i,c in enumerate(word):
                
                if pattern[i] not in d:
                    if c not in _d:
                        _d[c] = pattern[i]
                        d[pattern[i]] = c
                    else:
                        ok = False
                        break
                    continue
                    
                if d[pattern[i]] != c or _d[c] != pattern[i]:
                    ok = False
                    break
            
            if ok:
                ans.append(word)
            
        return ans
