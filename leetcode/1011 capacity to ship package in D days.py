def shipWithinDays(self, w: List[int], D: int) -> int:
        l, h = 1, sum(w)
        
        def ok(t):
            c, d = 0, 0
            
            for x in w:
                if x > t:
                    return False
                
                if c + x > t:
                    d += 1
                    c = x
                    continue
                c += x
            # print(t, d<D)
            return d < D
        
        ans = 999999999
        while l <= h:
            mid = (l + h)//2
            if ok(mid):
                ans = min(ans, mid)
                h = mid-1
            else:
                l = mid + 1
        
        return ans
