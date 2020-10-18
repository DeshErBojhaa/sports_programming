def totalFruit(self, tree: List[int]) -> int:
        if len(tree) < 3:
            return len(tree)
        if len(set(tree)) <= 2:
            return len(tree)
        
        lo, ans = 0, 0
        for i, v in enumerate(tree):
            while len(set(tree[lo:i+1])) > 2:
                lo += 1
            unq = len(set(tree[lo:i+1]))
            if unq <= 2:
                ans = max(ans, i-lo+1)
        return ans
