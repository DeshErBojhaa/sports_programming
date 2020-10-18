class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', '}': '{', ']':'['}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if x != d[c]:
                    return False
        
        if len(stack):
            return False
        return True
