def camelMatch(self, queries: List[str], p: str) -> List[bool]:
        
        def match(pat, s, ss):
            if pat == len(p) and s == len(ss):
                return True
            if pat == len(p):
                return not any(ord(x) < 91 for x in ss[s+1:])
            if s == len(ss):
                return False
            
            # Capital letter, Must match
            if ord(ss[s]) < 91:
                if p[pat] != ss[s]:
                    return False
                return match(pat+1, s+1, ss)
            
            # Small letter, Match if possible
            if ord(ss[s]) > 96:
                if p[pat] == ss[s]:
                    return match(pat+1, s+1, ss)
                return match(pat, s+1, ss)
            
        ans = [match(0, 0, q) for q in queries]
            
        return ans
