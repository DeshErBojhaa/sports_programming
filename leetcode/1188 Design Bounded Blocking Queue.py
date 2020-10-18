# 1188. Design Bounded Blocking Queue
from queue import SimpleQueue
from threading import Lock
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.enque_lock = Lock()
        self.deque_lock = Lock()
        self.cap = capacity
        self.q = SimpleQueue()
        self.deque_lock.acquire()

    def enqueue(self, element: int) -> None:
        self.enque_lock.acquire()
        self.q.put(element)
        
        if self.q.qsize() < self.cap:
            self.enque_lock.release()
        
        if self.deque_lock.locked():
            self.deque_lock.release()

    def dequeue(self) -> int:
        self.deque_lock.acquire()
        val = None
        
        if self.q.qsize() > 0:
            val = self.q.get()
        
        if self.q.qsize():
            self.deque_lock.release()
        
        if val and self.enque_lock.locked():
            self.enque_lock.release()
        return val

    def size(self) -> int:
        return self.q.qsize()
