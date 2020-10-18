# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root or not target or K<0:
            return []
        explored = set()
        path_to_root = []
        
        def trav(cur):
            if not cur:
                return False
            path_to_root.append(cur)
            if cur.val == target.val:
                return True
            found = trav(cur.left)
            if found:
                return found
            found = trav(cur.right)
            if not found:
                path_to_root.pop()
            return found
        
        ans = []
        def find(cur, dis):
            if not cur or dis < 0 or cur.val in explored:
                return
            if dis == 0:
                ans.append(cur.val)
                return
            find(cur.left, dis-1)
            find(cur.right, dis-1)
            
        trav(root)
        
        
        while path_to_root:
            cur = path_to_root.pop()
            # print(cur)
            find(cur, K)
            explored.add(cur.val)
            K -= 1
        
        return ans
