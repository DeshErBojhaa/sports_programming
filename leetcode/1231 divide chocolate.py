def maximizeSweetness(self, s: List[int], K: int) -> int:
        l, h = 0, sum(s)
        
        while l <= h:
            m = (h+l)//2
            chunk, sn = 0, 0
            
            for i in s:
                if i+sn >= m:
                    chunk += 1
                    sn = 0
                    continue
                sn += i
            
            #print(l, m, h, chunk, sn)
            if sn >= m:
                chunk += 1
            
            
            if chunk > K:
                l = m + 1
            else:
                h = m -1
        #print(l, h)
        return h
