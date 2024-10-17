class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        ans = num[::]
        for i in range(len(ans)):
            for j in range(i+1, len(num)):
                tmp = num[::]
                tmp[i], tmp[j] = tmp[j], tmp[i]
                ans = max(ans, tmp)
        return int(''.join(ans))
