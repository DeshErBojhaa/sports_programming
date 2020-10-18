class Solution:
    def calculate(self, s: str) -> int:
        ss = ''
        for c in s:
            if not c.isnumeric():
                ss += ' ' + c + ' '
            else:
                ss += c
        s = ss.split()
        
        stack = []
        for c in s:
            if c.isnumeric():
                stack.append(int(c))
            else:
                stack.append(c)
            if len(stack) > 2 and str(stack[-2]) in '/*':
                b = int(stack.pop())
                v = stack.pop()
                a = int(stack.pop())
                
                if v == '*':
                    stack.append(a*b)
                else:
                    stack.append(a//b)
        # print(stack)
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '-':
                stack[i] = '+'
                stack[i+1] *= -1
                
        while len(stack) > 1:
            b = int(stack.pop())
            v = stack.pop()
            a = int(stack.pop())
            if v == '+':
                stack.append(a+b)
            else:
                stack.append(a - b)
                
        return stack[-1]
