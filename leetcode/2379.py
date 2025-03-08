class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        acc = list(accumulate([int(x=='B') for x in blocks]))
        acc = [0] + acc
        ans = len(blocks)
        for i in range(1, len(acc)-k+1):
            j = i + k - 1
            cnt = acc[j] - acc[i - 1]
            if cnt >= k:
                return 0
            rem = k - cnt
            # print(i, j, cnt, rem)
            ans = min(ans, rem)
        return ans
