# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        
        k %= l
        
        while k:
            cv = head.val
            cur = head.next
            while cur:
                cur_val = cur.val
                cur.val = cv
                cv = cur_val
                cur = cur.next
            
            head.val = cv
            k -= 1
        return head
