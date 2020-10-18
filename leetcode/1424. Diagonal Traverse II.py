# 1424. Diagonal Traverse II
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        mx = 0
        store = defaultdict(list)
        
        for i, r in enumerate(nums):
            for j, v in enumerate(r):
                store[i+j].append(v)
                mx = max(mx, i+j)
        
        ans = []
        for i in range(mx+1):
            ans.extend(store[i][::-1])
        
        return ans
