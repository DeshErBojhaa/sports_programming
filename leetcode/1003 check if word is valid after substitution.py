def isValid(self, S: str) -> bool:
        stack = []
        
        for c in S:
            stack.append(c)
            while len(stack) > 2 and ''.join(stack[-3:]) == 'abc':
                stack = stack[:-3]
        
        if not stack:
            return True
        if len(stack) == 3 and ''.join(stack) == 'abc':
            return True
        return False
