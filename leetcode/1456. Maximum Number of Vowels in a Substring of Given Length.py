# 1456. Maximum Number of Vowels in a Substring of Given Length
from collections import deque
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dq, ans, vowel_cnt = deque(), 0, 0
        
        for c in s:
            dq.append(c)
            if c in 'aeiou':
                vowel_cnt += 1
            if len(dq) > k:
                left_chr = dq.popleft()
                if left_chr in 'aeiou':
                    vowel_cnt -= 1
            
            ans = max(ans, vowel_cnt)
        
        return ans
