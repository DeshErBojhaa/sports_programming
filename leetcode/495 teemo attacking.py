def findPoisonedDuration(self, t: List[int], d: int) -> int:
        ans = 0
        if not t:
            return ans
        for i in range(len(t)-1):
            if t[i] + d > t[i+1]:
                ans += t[i+1] - t[i]
            else:
                ans += d
        
        return ans + d
