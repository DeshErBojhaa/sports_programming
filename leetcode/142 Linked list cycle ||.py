def detectCycle(self, head: ListNode) -> ListNode:
        walk, run = head, head
        begin = True
        while walk != run or begin:
            begin = False
            if not walk or not run or not walk.next or not run.next or not (run.next).next:
                return None
            walk = walk.next
            run = (run.next).next
        
        run = head
        while run != walk:
            run = run.next
            walk = walk.next
        return walk
