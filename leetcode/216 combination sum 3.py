def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        if k > 9:
            return ans
    
    
        def rec(rem, mask, last):
            if rem == 0 and bin(mask).count('1') == k:
                ans.append([i for i in range(10) if mask&(1<<i)])
                return
            if rem < 0 or bin(mask).count('1') == k:
                return
            
            for i in range(last+1, 10):
                rec(rem-i, mask|(1<<i), i)
                
        
        rec(n, 0, 0)
        return ans
