class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mask, ans = 0, 0
        c = Counter()
        # d = defaultdict(int)
        l= 0
        for i, ch in enumerate(s):
            c[ch] += 1
            # print(set(c), set('abc'))
            while l < i and set(c) == set('abc'):
                c[s[l]] -= 1
                if c[s[l]] == 0:
                    del c[s[l]]
                l += 1
            ans += l
        
        return ans
