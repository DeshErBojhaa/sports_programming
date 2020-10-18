# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        a = head
        b = head.next
        new_head = b
        while b:
            new_head = b
            c = b.next
            b.next = a
            a = b
            b = c
        
        head.next = None
        return new_head
        
