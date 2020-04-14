from collections import deque
class Node:
    def __init__(self, key):
        self.k = key
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.N = capacity
        self.head = Node(-10000)
        self.tail = Node(10000)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        self.node_cache = {}

    def get(self, key: int) -> int:
        if not key in self.d:
            return -1
        
        nd = self.node_cache[key]
        # O->N->P
        # O<-N<-P
        nxt = nd.next
        prev = nd.prev
        nxt.prev = prev
        prev.next = nxt
        
        self.head.next.prev = nd
        nd.next = self.head.next
        self.head.next = nd
        nd.prev = self.head
        
        return self.d[key]
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            nd = self.node_cache[key]
            nd.prev.next = nd.next
            nd.next.prev = nd.prev
            
            self.head.next.prev = nd
            nd.next = self.head.next
            self.head.next = nd
            nd.prev = self.head
            return
        
        if len(self.d) == self.N:
            last_node = self.tail.prev
            last_node.prev.next = self.tail
            self.tail.prev = last_node.prev
            
            k = last_node.k
            del self.d[k]
            del self.node_cache[k]
        
        new_node = Node(key)
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        self.d[key] = value
        self.node_cache[key] = new_node
