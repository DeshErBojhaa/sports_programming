class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def trav(cur, lev=1):
            if not cur:
                return
            if len(ans) < lev:
                ans.append([])
            ans[lev-1].append(cur.val)
            trav(cur.left, lev+1)
            trav(cur.right, lev+1)
        
        trav(root)
        return ans
