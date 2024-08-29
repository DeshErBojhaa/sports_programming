from functools import cache
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mcc(root) -> int:
    @cache
    def rec(cur, me_must=False, par_cam=False):
        if not cur:
            return 0

        if me_must:
            return rec(cur.left, False, True) + rec(cur.right, False, True) + 1

        # if I am a leaf and my parent was not covered; cover me
        if cur.left is None and cur.right is None:
            return int( not par_cam)

        y, z = inf, inf
        # Place a camera here
        x = rec(cur.left, False, True) + rec(cur.right, False, True) + 1 # Cover me

        # Parent was not covered
        if not par_cam:
            # See if I can be covered by child.
            if cur.left:
                y = rec(cur.left, True, False) + rec(cur.right, False, False)
            if cur.right:
                z = rec(cur.left, False, False) + rec(cur.right, True, False)
            y = min(y, z)

        if par_cam:
            y = rec(cur.left, False, False) + rec(cur.right, False, False)


        return min(x, y)

    return min(rec(root, False, False), inf)

