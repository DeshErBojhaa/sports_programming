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

        d, _d, i = {}, {}, 0
        x = head
        while x:
            d[i] = Node(x.val)
            _d[x] = i
            x = x.next
            i += 1
        
        x = head
        while x:
            nd = d[_d[x]]
            if x.next:
                nd.next = d[_d[x.next]]
            if x.random:
                nd.random = d[_d[x.random]]
            x = x.next
        return d[0]
