from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s) < len(p):
            return []
        pc = Counter(p)
        sc = Counter(s[:len(p)])
        left = 0
        ans = []
        for i, c in enumerate(s[len(p):], len(p)):
            if sc == pc:
                ans.append(left)
            sc += {c:1}
            # print(sc, i, left, len(p))
            if i - left >= len(p):
                sc -= {s[left]: 1}
                left += 1
            
        if sc == pc:
            ans.append(left)
        return ans
