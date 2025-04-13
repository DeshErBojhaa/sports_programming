class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even, odd = 5, 4
        evn_cnt, odd_cnt = (n + 1) // 2, n // 2
        mod = 10 ** 9 + 7
        cc = pow(even, evn_cnt, mod)
        dd = pow(odd, odd_cnt, mod)
        # print(evn_cnt, even, odd_cnt, odd, cc, dd)
        return (cc * dd) % mod
