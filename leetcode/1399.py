class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(list)
        mx = 0
        for i in range(1, n+1):
            sm = sum(int(x) for x in str(i))
            d[sm].append(i)
            mx = max(mx, len(d[sm]))
        
        ans = 0
        for i in range(1, n+1):
            if len(d[i]) == mx:
                ans += 1
        
        return ans
