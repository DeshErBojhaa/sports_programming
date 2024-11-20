class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        N = len(s)
        a_l, b_l, c_l, a_r, b_r, c_r = [0] * N, [0] * N, [0] * N, [0] * N, [0] * N, [0] * N

        for i, c in enumerate(s):
            a_l[i] += a_l[i-1] + int(c == 'a')
            b_l[i] += b_l[i-1] + int(c == 'b')
            c_l[i] += c_l[i-1] + int(c == 'c')
        
        for i in range(N - 1, -1, -1):
            c = s[i]
            if i == N - 1:
                a_r[i] = int(c == 'a')
                b_r[i] = int(c == 'b')
                c_r[i] = int(c == 'c')
                continue
            a_r[i] = a_r[i+1] + int(c == 'a')
            b_r[i] = b_r[i+1] + int(c == 'b')
            c_r[i] = c_r[i+1] + int(c == 'c')
        
        if a_l[-1] < k or b_l[-1] < k or c_l[-1] < k:
            return -1

        ans = N
        for i in range(N-1, -1, -1):
            r = N - i
            l = 0
            for left, right in [(a_l, a_r), (b_l, b_r), (c_l, c_r)]:
                rem = k - right[i]
                l = max(l, bisect_left(left, rem))
                
            ans = min(ans, r + l + 1)
        
        for i in range(N):
            if a_l[i] >= k and b_l[i] >= k and c_l[i] >= k:
                ans = min(ans, i + 1)
                break
        for i in range(N-1, -1, -1):
            if a_r[i] >= k and b_r[i] >= k and c_r[i] >= k:
                r = N - i
                ans = min(ans, r)
                break
        return ans
