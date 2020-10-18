def matrixScore(self, A: List[List[int]]) -> int:
        for l in A:
            if l[0] == 0:
                for i in range(len(l)):
                    l[i] = 1 - l[i]
        
        for c in range(1, len(A[0])):
            zero = 0
            for r in range(len(A)):
                zero += int(A[r][c] == 0)
            if zero * 2 > len(A):
                for r in range(len(A)):
                    A[r][c] = 1 - A[r][c]
        ans = 0
        for s in A:
            ans += int("".join(str(x) for x in s), 2)
        
        # print(A)
        return ans
