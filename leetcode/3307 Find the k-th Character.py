class Solution:
    def kthCharacter(self, k: int, op: List[int]) -> str:
        pp, cnt = 1, 1
        while pp * 2 < k:
            pp *= 2
            cnt += 1
        k -= 1
        op = op[:cnt]
        ans = 0
        for o in op[::-1]:
            ans += (k >= pp and o)
            ans %= 26
            k = k % pp
            pp //= 2
            if pp == 0:
                break

        ch = chr(ord('a') + ans)
        return ch
