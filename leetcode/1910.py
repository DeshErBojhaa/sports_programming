class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack, p, np = [], list(part), len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= np and stack[-np:] == p:
                stack = stack[:-np]
        return ''.join(stack)
