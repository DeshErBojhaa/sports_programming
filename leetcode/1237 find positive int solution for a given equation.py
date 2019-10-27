def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        a, b, ans = 1, 1000, []
        while a <= 1000 and b >= 1:
            if customfunction.f(a,b) == z:
                ans.append([a,b])
                a += 1
                b -= 1
            if customfunction.f(a,b) > z:
                b -= 1
            if customfunction.f(a,b) < z:
                a += 1
        return ans
