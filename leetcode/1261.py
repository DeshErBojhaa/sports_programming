# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        fill(root, 0)

    def find(self, target: int) -> bool:
        return find(self.root, target)

def find(cur, target: int) -> bool:
    if cur is None:
        return False
    if cur.val == target:
        return True
    if find(cur.left, target):
        return True
    if find(cur.right, target):
        return True
    return False

def fill(cur, val):
    if cur is None:
        return
    cur.val = val
    fill(cur.left, val * 2 + 1)
    fill(cur.right, val * 2 + 2)
    


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
