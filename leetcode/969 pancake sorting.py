def pancakeSort(self, A: List[int]) -> List[int]:
        i = len(A)
        ans = []
        while i:
            if i == A[i-1]:
                i -= 1
                continue
            ind = A.index(i)
            A[:ind+1] = A[:ind+1][::-1]
            ans.append(ind+1)
            A[:i] = A[:i][::-1]
            ans.append(i)
            i -= 1
            
            # print(A)
        return ans
