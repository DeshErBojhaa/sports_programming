# 1573. Number of Ways to Split a String
class Solution:
    def numWays(self, s: str) -> int:
        ones = s.count('1')
        if ones%3:
            return 0
        if not ones:
            return comb(len(s)-1, 2)%(10**9+7)
        
        want = ones // 3
        
        buf1, buf2 = 0, 0
        ans, cnt = 0, 0
        
        for ch in s:
            cnt += int(ch == '1')
            buf1 += (cnt == want)
            buf2 += (cnt == want + want)
            
        return (buf1 * buf2)%(10**9+7)
