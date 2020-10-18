# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nd = root
        self.stack = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.nd:
            self.stack.append(self.nd)
            self.nd = self.nd.left
        top = self.stack.pop()
        self.nd = top.right
        return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.nd or self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
