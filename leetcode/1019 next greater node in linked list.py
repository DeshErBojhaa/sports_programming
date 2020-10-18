def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack, ans, i = [], [], 0
        
        while head:
            while len(ans) <= i:
                ans.append(0)
                
            while stack and stack[-1][0] < head.val:
                ans[stack[-1][1]] = head.val
                stack.pop()
            stack.append((head.val, i))
            
            head = head.next
            i += 1
        return ans
