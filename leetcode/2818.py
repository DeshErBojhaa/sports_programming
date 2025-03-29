class Solution:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
    def maximumScore(self, nums: List[int], k: int) -> int:
        def get_uf(x):
            if x < 2:
                return 0
            cnt = 0
            for v in Solution.primes:
                if v > x:
                    break
                if x % v:
                    continue
                cnt += 1
                while x % v == 0:
                    x //= v
            if x > 1:
                cnt += 1
            return max(1, cnt)
        pms = [get_uf(x) for x in nums]

        N = len(nums)
        r_contrib, l_contrib = [0] * (N + 1), [0] * (N+1)
        stack = [[1000000, N]]

        for i in range(N-1, -1, -1):
            while stack and pms[i] >=  stack[-1][0]:
                stack.pop()
            ln = stack[-1][1] - i - 1
            r_contrib[i] = ln
            stack.append([pms[i], i])
        
        stack = []
        for i in range(N):
            while stack and pms[i] > stack[-1][0]:
                stack.pop()
            ln = i + 1
            if stack:
                ln = i - stack[-1][1]
            l_contrib[i] = ln
            stack.append([pms[i], i])
        
        contribution = [a + a*b for a, b in zip(l_contrib, r_contrib)]
        heap = [(-x, l) for x, l in zip(nums, contribution)]
        heapify(heap)
        ans = 1

        mod = int(1e9+7)
        while k and heap:
            v, cnt = heappop(heap)
            v *= -1
            cnt = min(k, cnt)
            ans *= pow(v, cnt, mod)
            if ans > mod:
                ans %= mod
            k -= cnt
        return ans
