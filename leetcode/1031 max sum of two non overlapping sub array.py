def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        a, n = list(accumulate(A)), len(A)
        ans = -9999999999
        print(a)
        for i in range(n):
            for j in range(n):
                # Take L at i and M at j
                if i < j:
                    if i + L <= j and j + M <= n:
                        l = a[i+L-1] - (a[i-1] if i else 0)
                        m = a[j+M-1] - a[j-1]
                        ans = max(ans, l+m)
                if i > j:
                    if i + L <= n and j + M <= i:
                        l = a[i+L-1] - a[i-1]
                        m = a[j+M-1] - (a[j-1] if j else 0)
                        ans = max(ans, l+m)
        return ans
                
