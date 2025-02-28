class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        na, nb = len(str1), len(str2)
        @cache
        def rec(a, b):
            if a == na:
                return nb - b
            if b == nb:
                return na - a
            
            ans = inf
            if str1[a] == str2[b]:
                ans = rec(a+1, b+1) + 1
            else:
                ans = rec(a+1, b) + 1
                ans = min(ans, rec(a, b + 1) + 1)

            return ans

        ln = rec(0, 0)

        @cache
        def path(a, b):
            if a == na:
                return str2[b:]
            if b == nb:
                return str1[a:]
            
            rec_ab = rec(a, b)
            if str1[a] == str2[b]:
                x = rec(a+1, b+1)
                if x + 1 == rec_ab:
                    return str1[a] + path(a+1, b+1)

            x = rec(a+1, b)
            y = rec(a, b+1)
            if x + 1 == rec(a, b):
                return str1[a] + path(a+1, b)
            else:
                return str2[b] + path(a, b+1)
                

        return path(0, 0)
