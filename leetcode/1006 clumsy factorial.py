def clumsy(self, N: int) -> int:
        a, x = [], 0
        
        for i, v in enumerate(range(N, 0, -1)):
            
            if i%4 == 0:
                x = v
                
            if i%4 == 1:
                x *= v
                
            if i%4 == 2:
                x //= v
                
            if i%4 == 3:
                a.append(x)
                a.append(v)
                x = 0
            
        if x!= 0:
            a.append(x)
            
        ans = 0
        for i, v in enumerate(a[1:]):
            if i%2 == 0:
                ans += v
            else:
                ans -= v
        
        return ans + a[0]
