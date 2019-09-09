    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        p = preorder
        stack = []
        
        # Make the root node
        root = TreeNode(p[0])
        stack.append(root)
        
        hand = None
        
        for idx in range(1,len(p)):
            cur = p[idx]
            x = TreeNode(cur)
            # Add to the left
            if cur < stack[-1].val:
                stack[-1].left = x
                stack.append(x)
                continue
            while stack and stack[-1].val < cur:
                hand = stack.pop()
                if not stack or cur < stack[-1].val:
                    hand.right = x
                    stack.append(x)
        return root
