def missingNumber(self, a: List[int]) -> int:
        d = (a[-1] - a[0])//len(a)
        
        for i in range(1, len(a)):
            if a[i] - d != a[i-1]:
                return a[i] - d
        return 0
