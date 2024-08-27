class Solution:
    def countPairs(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort(reverse = True, key = lambda x: len(str(x)))

        def combinations(n):
            n, s = list(str(n)), {n}
            for i in range(len(n)):
                for j in range(i+1, len(n)):
                    n[i], n[j] = n[j], n[i]
                    x = int(''.join(n))
                    n[i], n[j] = n[j], n[i]
                    s.add(x)
            return s

        c, ans = Counter(), 0
        for i, n in enumerate(nums):
            ans += c[n]
            o = combinations(n)
            oo = set(o)
            for x in o:
                oo = oo.union(combinations(x))
            c += Counter(oo)

        return ans
