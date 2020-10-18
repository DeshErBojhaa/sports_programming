# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    
    def compress(self, l):
        compressed = ''
        for v in l:
            cmp = ''
            for i in range(4):
                least_significant_byte = (v >> (i*8)) & 255
                char_8_bit = chr(least_significant_byte)
                cmp = char_8_bit + cmp
            compressed += cmp
        return compressed
    
    def decompress(self, s):
        ans = []
        for i in range(len(s)//4):
            st = i * 4
            ed = st + 4
            
            cur_s = s[st:ed]
            
            tmp_val = 0
            
            for v in cur_s:
                tmp_val = tmp_val * 256 + ord(v)
            ans.append(str(tmp_val))
        return ','.join(ans)
            
        
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def preorder(cur):
            if not cur:
                return
            nonlocal ans
            ans.append(cur.val) 
            preorder(cur.left)
            preorder(cur.right)
        preorder(root)
        return self.compress(ans)
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        # print(data.split(','))
        data = self.decompress(data)
        q = deque(map(int, data.split(',')))
        root = TreeNode(int(q.popleft()))
        
        stack = [root]
        
        while q:
            cur_val = q.popleft()
            
            last_element = None
            while stack and stack[-1].val < cur_val:
                last_element = stack.pop()
            
            cur_node = TreeNode(cur_val)
            if last_element is None:
                stack[-1].left = cur_node
            else:
                last_element.right = cur_node
            
            stack.append(cur_node)
            
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
