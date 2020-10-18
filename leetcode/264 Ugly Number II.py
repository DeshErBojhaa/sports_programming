# 264. Ugly Number II
class Solution:
    cur = {1}
    nxt = set()
    ugly = [1]

    while len(cur) <1690:

        for i in (2, 3, 5):
            for x in cur:
                if x * i < 2**31:
                    nxt.add(x * i)

        # ugly.extend(nxt)
        cur = set(nxt)

    ugly.extend(cur)
    ugly.sort()
    # print(sorted(ugly))
    def nthUglyNumber(self, n: int) -> int:
        
        return Solution.ugly[n - 1]
