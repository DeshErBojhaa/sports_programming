# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        def rec(cur):
            if not cur:
                return
            dist = abs(cur.val - target)
            heappush(heap, [dist, cur.val])
            rec(cur.left)
            rec(cur.right)
        rec(root)

        return [x[1] for x in heapq.nsmallest(k, heap)]
