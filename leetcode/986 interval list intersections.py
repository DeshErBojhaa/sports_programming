 def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(A) and j < len(B):
            # There are total 5 cases
            # 1. Same interval
            if A[i] == B[j]:
                ans.append(A[i])
                i += 1
                j += 1
                continue
            
            # 2. A covers B
            ################### . A
            #   ############      B
            if A[i][0] <= B[j][0] and A[i][1] >= B[j][1]:
                ans.append(B[j])
                j += 1
                continue
            
            # 3. B covers A
            #      #######     A
            ################## B
            if A[i][0] >= B[j][0] and A[i][1] <= B[j][1]:
                ans.append(A[i])
                i += 1
                continue
            
            # 4. A is left of B
            ############         A
            #    ##############   B
            if A[i][1] >= B[j][0] and A[i][1] <= B[j][1]:
                ans.append([B[j][0],A[i][1]])
                i += 1
                continue
            # 5. A is right of B
            #        ##############
            # #############
            if A[i][0] >= B[j][0] and A[i][0] <= B[j][1]:
                ans.append([A[i][0], B[j][1]])
                j += 1
                continue
            if A[i][1] < B[j][0]:
                i += 1
                continue
            j += 1
        return ans
