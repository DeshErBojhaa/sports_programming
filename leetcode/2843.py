class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for n in range(low, high+1):
            n = deque(str(n))
            if len(n)%2== 1:
                continue
            sm = 0
            while n:
                sm += int(n[0]) - int(n[-1])
                n.pop()
                n.popleft()
            ans += sm == 0
        
        return ans
