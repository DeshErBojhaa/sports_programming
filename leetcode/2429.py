class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        s1 = bin(num1)[2:]
        n = len(s1)
        ans = ['0'] * n
        cnt1 = s1.count('1')
        cnt2 = bin(num2).count('1')
        for i in range(n):
            v = s1[i]
            if cnt2 == 0:
                break
            if v == '1':
                ans[i] = '1'
                cnt2 -= 1
        for i in range(n-1, -1, -1):
            v = s1[i]
            if cnt2 == 0:
                break
            if v == '0':
                ans[i] = '1'
                cnt2 -= 1
        
        ss = ''.join(ans)
        ss = '1' * cnt2 + ss
        
        return int(ss, 2)

        
