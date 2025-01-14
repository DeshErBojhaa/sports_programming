class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        cnt, cmn, ans, idx = [0] * (n + 1), 0, [None] * n, 0
        for a, b in zip(A, B):
            cnt[a] += 1
            cnt[b] += 1
            if a != b:
                cmn += cnt[a] == 2
            cmn += cnt[b] == 2
            ans[idx] = cmn
            idx += 1
        return ans
