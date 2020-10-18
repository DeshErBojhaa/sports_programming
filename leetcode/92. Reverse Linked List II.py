# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 92. Reverse Linked List II
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        index, nxt, cur = 0, None, head
        stack = []
        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev = dummy_head
        
        while cur:
            next_ = cur.next
            index += 1
            if index < m:
                prev = cur
            if index == n + 1:
                nxt = cur
            
            if index >= m and index <= n:
                if stack:
                    cur.next = stack[-1]    
                stack.append(cur)
                
            cur = next_
        
        prev.next = stack[-1]
        stack[0].next = nxt
        
        return dummy_head.next
