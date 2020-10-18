"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        # Without extra space.
        x = head
        while x:
            copy = Node(x.val)
            copy.next = x.next
            x.next = copy
            x = copy.next
        
        x = head
        while x:
            x.next.random = x.random and x.random.next
            x = x.next.next
        
        nh = head.next
        while head:
            original_next = head.next.next
            head.next.next = original_next and original_next.next
            head = original_next
        return nh
