# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1597. Build Binary Expression Tree From Infix Expression
class Solution:
    def expTree(self, s: str) -> 'Node':
        N = len(s)
        precedence = {'-':1,'+':1,'*':2,'/':2, '(': 0}
        
        stk = []
        postfix = ''
        
        # convert to postfix
        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(ch)
            elif ch.isdigit():
                postfix += ch
            elif ch == ')':
                while stk and stk[-1] != '(':
                    postfix += stk.pop()
                stk.pop()
            # Now and Operator is found
            elif ch in '+-*/':
                while stk and precedence[ch] <= precedence[stk[-1]]:
                    postfix += stk.pop()
                stk.append(ch)
        
        while stk:
            postfix += stk.pop()
        
        stk = []
        
        for ch in postfix:
            if ch.isdigit():
                stk.append(Node(ch))
            else:
                cur = Node(ch)
                cur.right = stk.pop()
                cur.left = stk.pop()
                
                stk.append(cur)
                
        return stk.pop()
