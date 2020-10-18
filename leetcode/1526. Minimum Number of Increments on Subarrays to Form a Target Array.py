# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(max(0, a-b) for a, b in zip(target, [0]+target))
