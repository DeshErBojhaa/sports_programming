# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def str_sum(a, b):
            if len(a) < len(b):
                a, b = b, a
            ans, carry = [], 0
            b = '0' * (len(a) - len(b)) + b

            for x, y in zip(reversed(a), reversed(b)):
                add = int(x) + int(y) + carry
                ans.append(add % 10)
                carry = int(add > 9)
            if carry:
                ans.append(1)

            return ''.join(reversed([str(x) for x in ans]))
        
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        num1, num2 = num1[::-1], num2[::-1]
        ans = '0'
        carry = 0
        
        for i in range(len(num2)):
            x = int(num2[i])
            carry, tmp_ans = 0, []
            for j in range(len(num1)):
                sm = x * int(num1[j]) + carry
                tmp_ans.append(sm%10)
                carry = sm // 10
            
            if carry:
                tmp_ans.append(carry)
                
            tmp_ans = tmp_ans[::-1]
                  
            for j in range(i):
                tmp_ans.append(0)

            ans = str_sum(ans, ''.join(map(str,tmp_ans)))
            
                
        return ans
