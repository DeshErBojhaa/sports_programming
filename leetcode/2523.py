class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes, diff, ans = [], inf, [-1, -1]

        def ok(n):
            for i in range(2, n):
                if i * i > n:
                    break
                if n % i == 0:
                    return False
            return True

        left = max(left, 2)
        for i in range(left, right + 1):
            if not ok(i):
                continue
            primes.append(i)
            if len(primes) > 1 and primes[-1] - primes[-2] < diff:
                diff = primes[-1] - primes[-2]
                ans = [primes[-2], primes[-1]]
                if diff <= 2:
                    return ans
        return ans
