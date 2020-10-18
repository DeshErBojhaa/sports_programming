# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 82. Remove Duplicates from Sorted List II
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur, ret = head, ListNode(None)
        last_dup, sudo_head = None, ret
        
        while cur:
            # print(cur.val, cur.next.val if cur.next else 'X', ret.val)
            if cur.next and cur.val == cur.next.val:
                last_dup = cur.val
            elif cur.next and cur.val != cur.next.val and cur.val != last_dup:
                ret.next = ListNode(cur.val)
                ret = ret.next  
            elif not cur.next and cur.val != last_dup:
                ret.next = ListNode(cur.val)

            cur = cur.next
        
        return sudo_head.next
        
