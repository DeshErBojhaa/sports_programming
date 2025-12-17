class Solution:
    def minOperations(self, n: int) -> int:
        p = [1] * 21
        for i in range(1, 21):
            p[i] = p[i-1] * 2
        # print(p)
        steps = 0
        while n > 0:
            i = bisect_left(p, n)
            red = n - p[i-1] if p[i] > n else p[i]
            add = p[i] - n
            if red < add:
                n = red
            else:
                n = add
            steps += 1

        return steps
