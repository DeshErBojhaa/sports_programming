def trav(cur, d, ans, par=None, child=None):
    if not cur:
        return
    
    if cur.val in d:
        if child == 0:
            par.left = None
        elif child == 1:
            par.right = None
    else:
        if par and par.val in d:
            ans.append(cur)
    trav(cur.left, d, ans, cur, 0)
    trav(cur.right, d, ans, cur, 1)


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        d = set(to_delete)
        ans = []
        trav(root, d, ans)
        
        if root.val not in d:
            ans.append(root)
        return ans
