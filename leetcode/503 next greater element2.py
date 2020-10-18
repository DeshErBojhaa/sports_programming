def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk, ans = [], [-1]*len(nums)
        # First pass
        for i, v in enumerate(nums):
            while stk and stk[-1][1] < v:
                ans[stk[-1][0]] = v
                stk.pop()
            stk.append([i, v])
        # Second pass
        for i, v in enumerate(nums):
            while stk and stk[-1][1] < v:
                ans[stk[-1][0]] = v
                stk.pop()
        
        return ans
