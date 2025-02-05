class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        a, b = list(s1), list(s2)
        n = len(a)

        for i in range(n):
            for j in range(i, n):
                a[i], a[j] = a[j], a[i]
                if a == b:
                    return True
                a[i], a[j] = a[j], a[i]
        return False
