def lis(nums):
    d = []
    nums.sort(key=lambda c: (c[0], -c[1]))
    for _, y in nums:
        if not d or y > d[-1]:
            d.append(y)
            continue
        d[bisect_left(d, y)] = y
    
    return len(d)

class Solution:
    def maxPathLength(self, cc: List[List[int]], k: int) -> int:
        ll = [(x, y) for x, y in cc if x < cc[k][0] and y < cc[k][1]]
        rr = [(x, y) for x, y in cc if x > cc[k][0] and y > cc[k][1]]
        return lis(ll) + 1 + lis(rr)
