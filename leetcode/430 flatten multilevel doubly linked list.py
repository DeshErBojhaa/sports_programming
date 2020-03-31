"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def _flatten(cur):
            if not cur:
                return None
            if not cur.next and not cur.child:
                return cur
            
            next_in_original = cur.next
            if cur.child:
                cur.next = cur.child   # Cur -> Child
                cur.child.prev = cur   # Cur <- Child
                last_node_in_child_list = _flatten(cur.child)
                cur.child = None
                if last_node_in_child_list:
                    last_node_in_child_list.next = next_in_original  # Child_last -> Original Next
                if next_in_original:
                    next_in_original.prev = last_node_in_child_list  # Child_last <- Original Next 
            
            return _flatten(next_in_original)
        
        _flatten(head)
        return head
