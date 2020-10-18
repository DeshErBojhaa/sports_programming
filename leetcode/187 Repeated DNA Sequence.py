from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        ss = s
        s = [ord(c)-64 for c in s]
        ans = set()
        alphabates = 4
        mp = 4 ** 9
        
        _hash = 0
        for i in range(10):
            _hash = (alphabates * _hash + s[i])
        all_hash = defaultdict(set)
        all_hash[_hash].add(ss[:10])
        
        for i in range(10, len(s)): # Go from 11th char to the last char
            _hash = (alphabates * (_hash - s[i-10] * mp) + s[i] )
            cur_str = ss[i-9:i+1]
            if _hash in all_hash:
                if cur_str in all_hash[_hash]:
                    ans.add(cur_str)
            all_hash[_hash].add(cur_str)
        return list(ans)
