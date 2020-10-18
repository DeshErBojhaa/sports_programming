# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop
class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if not any(lists):
            return None
        heap = []
        d = {}
        for ind, i in enumerate(lists):
            if not i:
                continue
            heappush(heap, (i.val, ind))
            d[ind] = i
        
        head = ListNode(0)
        cur = head
        while heap:
            top = heappop(heap)
            ind = top[1]
            
            cur.next = d[ind]
            cur = cur.next
            
            if d[ind]:
                nxt = d[ind].next
                if nxt:
                    heappush(heap, (nxt.val, ind))
                    d[ind] = nxt
        return head.next
