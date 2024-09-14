class Fen:
    def __init__(self, size):
        """Initialize a Fenwick Tree with a given size."""
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        """Update the Fenwick Tree with a value at a specific index."""
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, index):
        """Compute the prefix sum up to a specific index."""
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_sum(self, left, right):
        """Compute the sum of elements in a specific range [left, right]."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n, ans = len(nums), [0] * len(nums)
        arr = sorted([(v, i) for i, v in enumerate(nums)], reverse=True)
        fen = Fen(n)
        for v, i in arr:
            placed = fen.range_sum(i+1, n)
            ans[i] = n - i - placed - 1
            fen.update(i+1, 1)

        return ans
