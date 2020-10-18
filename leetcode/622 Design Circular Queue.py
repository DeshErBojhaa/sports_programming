# 622. Design Circular Queue
class Node:
    def __init__(self, v=0):
        self.V = v
        self.prev = None
        self.next = None
        

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.N = k
        self.cnt = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.cnt == self.N:
            return False
        self.cnt += 1
        beforetail = self.tail.prev
        curnode = Node(value)
        
        beforetail.next = curnode
        curnode.prev = beforetail
        
        self.tail.prev = curnode
        curnode.next = self.tail
        
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.cnt == 0:
            return False
        self.cnt -= 1
        head_next_next = self.head.next.next
        self.head.next = head_next_next
        head_next_next.prev = self.head
        
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.head.next.V

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.tail.prev.V

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.cnt == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.cnt == self.N


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
