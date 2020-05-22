# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 109. Convert Sorted List to Binary Search Tree
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 1. Get the len of the linked list
        # 2. Travarse the binary tree in inorder
        # 3. Have a global head pointer
        N, cur = 0, head
        while cur:
            cur = cur.next
            N += 1

        def build(l, r):
            if l > r:
                return None
            nonlocal head
            
            mid = (l + r) // 2
            l = build(l, mid-1)
            cur = TreeNode(head.val)
            head = head.next
            r = build(mid+1, r)
            
            cur.left = l
            cur.right = r
            
            return cur
        
        return build(0, N - 1)
            
