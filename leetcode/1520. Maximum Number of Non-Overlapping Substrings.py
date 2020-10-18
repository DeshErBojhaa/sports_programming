# 1520. Maximum Number of Non-Overlapping Substrings
class Solution:
    def maxNumOfSubstrings(self, ss: str) -> List[str]:
        s, e, span = [None] * 26, [float('-inf')] * 26, [float('-inf')] * 26
        
        for i, ch in enumerate(ss):
            idx = ord(ch) - 97
            if s[idx] is None:
                s[idx] = i
            e[idx] = i
            span[idx] = i - s[idx] + 1
        
        l = []
        for i in range(26):
            if s[i] is None:
                continue
            l.append((span[i], s[i], e[i], chr(97+i)))
        
        l.sort()
        ans = []
        seen = set()
        
        def process(st, ed):
            if st > ed:
                return []
            # print(st, ed)
            idx = st
            while idx <= ed:
                ch_ind = ord(ss[idx])-97
                ed = max(ed, e[ch_ind])
                if s[ch_ind] < st:
                    return process(s[ch_ind], ed)
                idx += 1
            
            return ss[st:ed+1]
        
        for _, start, end, ch in l:
            if ch in seen:
                continue
            seq = process(start, end)
            if seq:
                new_s = set(seq)
                if seen.isdisjoint(new_s):
                    ans.append(''.join(seq))
                    seen.update(seq)
            
        return ans


