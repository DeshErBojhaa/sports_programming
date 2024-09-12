class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = ''
        for i in range(0, len(s), k):
            sm = 0
            for c in s[i:i+k]:
                sm += ord(c) - ord('a')
            
            ans += chr(sm%26 + ord('a'))
        
        return ans
