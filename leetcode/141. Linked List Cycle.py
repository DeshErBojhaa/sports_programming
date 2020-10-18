# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        walker, runner = head, head
        
        while runner:
            walker = walker.next
            if runner.next:
                runner = runner.next.next
            else:
                runner = None
            if walker and walker == runner:
                return True
        
        return False
