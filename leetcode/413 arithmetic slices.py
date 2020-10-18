def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        ans = 0
        for i in range(len(A)-2):
            j, dis, prev = i+1, A[i+1] - A[i], A[i]
            while j < len(A) and A[j] - prev == dis:
                ans += int((j - i) >= 2)
                prev = A[j]
                j += 1
                    
                
        return ans
    
