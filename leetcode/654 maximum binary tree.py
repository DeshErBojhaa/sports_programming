def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        def make(l, r):
            if r - l < 1:
                return None
            
            m = max(nums[l:r])
            i = nums.index(m)
            
            cur = TreeNode(m)
            cur.left = make(l, i)
            cur.right = make(i+1, r)
            
            return cur
        
        return make(0, len(nums))
