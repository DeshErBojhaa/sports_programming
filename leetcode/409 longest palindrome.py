def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        modd, ans = 0, 0
        
        print(c)
        for i, v in c.items():
            if v%2:
                modd = 1
                ans += v-1
            else:
                ans += v
        return ans + modd
