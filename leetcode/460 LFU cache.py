class Node:
    def __init__(self, key, val):
        self.k = key
        self.v = val
        self.f = 1
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.N = capacity
        self.count = 0
        self.min_freq = 1
        self.max_freq = 1
        self.node_cache = {}
        self.freq_cache = {}

    def init_freq_cache(self, freq):
        head = Node(None, None)
        tail = Node(None, None)
        head.next = tail
        tail.prev = head
        self.freq_cache[freq] = (head, tail)
    
    def increase_freq_of_node(self, key):
        node = self.node_cache[key]
        next_freq = node.f + 1
        
        # Remove node from cur freq level
        node.prev.next = node.next
        node.next.prev = node.prev
        
        if next_freq not in self.freq_cache:
            self.init_freq_cache(next_freq)
        
        # Add node to the begining of freq cache
        head, tail = self.freq_cache[next_freq]
        node.next = head.next
        head.next.prev = node
        head.next = node
        node.prev = head
        
        # Increase node's frequenct
        node.f += 1
        self.max_freq = max(self.max_freq, node.f)
            
    def remove_node(self):
        for i in range(1, self.max_freq+1):
            h, t = self.freq_cache[i]
            if h.next != t:
                self.min_freq = i
                break
    
        self.count -= 1
        freq = self.min_freq
        head, tail = self.freq_cache[freq]
        node = tail.prev
        key = node.k
        # print('Removing', node.k, node.v)
        # Remove this node from freq_cache
        node.prev.next = tail
        tail.prev = node.prev
        
        # print('Removing', node.k, node.v)
        # Remove this node from node_cache
        del self.node_cache[key]
        

    def get(self, key: int) -> int:
        nd = self.node_cache.get(key, None)
        if not nd:
            return -1
        self.increase_freq_of_node(key)
        return nd.v

    def put(self, key: int, value: int) -> None:
        # Max capacity 0. Nothing to do
        if self.N == 0:
            return
        
        if key in self.node_cache:
            self.node_cache[key].v = value
            self.increase_freq_of_node(key)
            return
        
        # Delete node if capacity overflow
        if self.count >= self.N:
            self.remove_node()
        # print('Putting', key, value)    
        node = Node(key, value)
        
        # Add to freq_cache
        if 1 not in self.freq_cache:
            self.init_freq_cache(1)
        
        head, _ = self.freq_cache[1]
        node.next = head.next
        node.prev = head
        node.next.prev = node
        head.next = node
        
        # Add to node_cache
        self.node_cache[key] = node
        self.count += 1
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
