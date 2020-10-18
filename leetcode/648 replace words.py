def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict = sorted(dict)
        ds = sorted(dict, key=len)
        
        ws = sentence.split(' ')
        ans = []
        for w in ws:
            for d in ds:
                if len(d) > len(w):
                    continue
                if d == w[:len(d)]:
                    ans.append(d)
                    w = ''
                    break
            if w:
                ans.append(w)
        
        return ' '.join(ans)
