# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 328. Odd Even Linked List
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        zero = head
        zero_tail = head
        one = head.next
        tmp_one = head.next
        
        while one and zero:
            zero_tail = zero
            if zero.next:
                zero.next = zero.next.next
            if one.next:
                one.next = one.next.next
            
            zero = zero.next
            one = one.next
            
            if zero:
                zero_tail = zero
        
        zero_tail.next = tmp_one
        cur = head
        
        return head
