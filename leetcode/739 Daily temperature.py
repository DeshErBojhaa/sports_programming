def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        
        stack = []
        
        for i, v in enumerate(T):
            if not stack or v <= stack[-1][0]:
                stack.append((v,i))
                continue
            while stack and stack[-1][0] < v:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((v,i))
        
        return ans
