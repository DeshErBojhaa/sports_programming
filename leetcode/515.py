class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def rec(cur, l=1):
            if not cur:
                return
            if len(ans) < l:
                ans.append(cur.val)
            else:
                ans[l-1] = max(ans[l-1], cur.val)
            rec(cur.left, l+1)
            rec(cur.right, l+1)
        
        rec(root)
        return ans
