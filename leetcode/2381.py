class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cnt = [0] * (len(s) + 1)
        A = ord('a')
        for a, b, c in shifts:
            if c == 0:
                c = -1
            cnt[a] += c
            cnt[b+1] -= c
        cnt = list(accumulate(cnt))
        
        s = list(s)
        for i, c in enumerate(s):
            s[i] = chr((ord(c) - A + cnt[i])% 26 + ord('a'))
        return ''.join(s)
