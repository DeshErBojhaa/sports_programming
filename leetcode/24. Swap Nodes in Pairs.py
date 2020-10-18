# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 24. Swap Nodes in Pairs
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        zero = dummy
        while head:
            one = head
            two = head.next
            if not two:
                break
            three = two.next
            
            zero.next = two
            two.next = one
            one.next = three
            
            zero = one
            head = three
        
        return dummy.next
