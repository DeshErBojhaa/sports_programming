# 150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        stack = []
        
        for t in tokens:
            # print(stack)
            if t in op:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(op[t](a, b))
                continue
            stack.append(t)
        
        return stack[-1]
