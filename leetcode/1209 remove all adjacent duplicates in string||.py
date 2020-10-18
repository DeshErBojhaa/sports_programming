def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if not stack:
                stack.append([c, 1])
                continue
            if stack[-1][0] == c:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
                continue
            stack.append([c, 1])
        
        return ''.join(c*x for c,x in stack)
