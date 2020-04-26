# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import SimpleQueue
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = SimpleQueue()
        ans = str(root.val) + ','
        q.put(root)
        
        while q.qsize():
            top = q.get()
            l = top.left
            r = top.right
            
            if l:
                ans += str(l.val) + ','
                q.put(l)
            else:
                ans += '#,'
            
            if r:
                ans += str(r.val) + ','
                q.put(r)
            else:
                ans += '#,'
        return ans[:-1]
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        dq = deque(data)
        
        root = TreeNode(int(dq.popleft()))
        q = SimpleQueue()
        q.put(root)
        
        while dq:
            top = q.get()
            l = dq.popleft()
            r = None
            if dq:
                r = dq.popleft()
            if l != '#':
                top.left = TreeNode(int(l))
                q.put(top.left)
            if r != '#':
                top.right = TreeNode(int(r))
                q.put(top.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
