class Solution:
    def numEquivDominoPairs(self, dd: List[List[int]]) -> int:
        ans, c = 0, Counter()

        for i in range(len(dd)):
            tp = (dd[i][0], dd[i][1])
            if dd[i][0] > dd[i][1]:
                tp = (dd[i][1], dd[i][0])
            c[tp] += 1

        for v in c.values():
            ans += (v * (v-1))//2
        return ans
