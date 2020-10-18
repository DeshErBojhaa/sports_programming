# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 
# 19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur, behind = head, head
        cnt, ln = 0, 0
        
        while cur:
            if cnt > n:
                behind = behind.next
            cur = cur.next
            cnt += 1
            ln += 1
        

        if ln == n:
            head = head.next
            return head
        
        if behind.next:
            behind.next = behind.next.next
        
        return head
