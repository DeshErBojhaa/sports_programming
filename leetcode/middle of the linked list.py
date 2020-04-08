# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        w, r = head, head
        while r.next and r.next.next:
            w = w.next
            r = r.next.next
        if r.next:
            w = w.next
        return w
