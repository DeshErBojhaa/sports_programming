"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 428. Serialize and Deserialize N-ary Tree
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        s = []
        unique_id = 0
        d = {}
        def trav(cur):
            nonlocal unique_id
            if not cur:
                return
            unique_id += 1
            copy_uid = unique_id
            d[str(unique_id)] = str(cur.val)
            
            for nxt in cur.children:
                nxt_uid = trav(nxt)
                s.append(f'{copy_uid, nxt_uid}')
            
            return copy_uid
        
        trav(root)
        
        k_list, v_list = ','.join(d.keys()), ','.join(d.values())
        relation = '#'.join(s)
        
        return k_list + '$' + v_list + '$' + relation

	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        if not data or data == '':
            return None
        
        d = {}
        data = data.split('$')
        data[0], data[1] = data[0].split(','), data[1].split(',')
        
        uid_to_val = {int(k):int(v) for k, v in zip(data[0], data[1])}   
        relations = data[2].split('#')
        
        root = Node(uid_to_val[1], [])
        d.setdefault(1, root)
        
        for x in relations:
        
            if not x:
                continue
            a, b = map(int,x.replace('(', '').replace(')', '').split(','))
        
            na = d.setdefault(a, Node(int(uid_to_val[a]), []))
            nb = d.setdefault(b, Node(int(uid_to_val[b]), []))
            
            na.children.append(nb)
            
            if root is None and a == 1:
                root = na
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
