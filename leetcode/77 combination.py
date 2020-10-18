class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def rec(num, cur):
            if not cur:
                cur = []
            if len(cur) == k:
                ans.append(cur[::])
                return
            for i in range(num, n+1):
                cur.append(i)
                rec(i+1, cur)
                cur.pop()
        
        rec(1, None)
        return ans
