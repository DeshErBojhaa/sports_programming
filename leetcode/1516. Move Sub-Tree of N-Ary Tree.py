"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
# 1516. Move Sub-Tree of N-Ary Tree
class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        parent = {}
        
        def trav(cur, par):
            if not cur:
                return
            parent[cur] = par
            
            for nxt in cur.children:
                trav(nxt, cur)
        
        trav(root, None)
        
        # Find type
        # 0 -> p is direct cild of q
        if parent[p] == q:
            return root
        
        typ = 1
        # Check if Q is a child of P
        q_par = parent[q]
        while q_par:
            if q_par == p:
                typ = 2
                break
            q_par = parent[q_par]
        
        if typ == 1:  # Q IS NOT a child of P Just move
            q.children.append(p)
            parent[p].children.pop(parent[p].children.index(p))
            return root
        
        # Now Type 2, q is a child of p
        p_par = parent[p]
        # Detouch Q from it's parent
        parent[q].children.pop(parent[q].children.index(q))
        
        # Detouch P from it's parent. Edge case ROOT
        if p_par:
            p_idx = p_par.children.index(p)
            p_par.children.pop(p_idx)
        
        # Set P as a child of Q
        q.children.append(p)
        
        # Append Q in P's parent
        if p_par:
            p_par.children.insert(p_idx, q)
        
        # P has a parent that means it was not the root
        if p_par:
            return root
        
        # P was the former root, so now Q will be the root
        return q
