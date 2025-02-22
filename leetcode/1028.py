# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, trav: str) -> Optional[TreeNode]:
        dd, num, depth = [], 0, 0
        for ch in trav:
            if ch == '-' and not num:
                depth += 1
            if ch == '-' and num:
                dd.append([num, depth])
                depth = 1
                num = 0
            if ch != '-':
                num *= 10
                num += int(ch, 10)
        
        dd.append([num, depth])

        stack = []
        for num, d in dd:
            if not stack:
                stack.append([TreeNode(num), d])
                continue
            while stack and stack[-1][1] + 1 != d:
                stack.pop()
            par = stack[-1][0]
            cur = TreeNode(num)
            if par.left is None:
                par.left = cur
            else:
                par.right = cur
            stack.append([cur, d])

        return stack[0][0]
        
