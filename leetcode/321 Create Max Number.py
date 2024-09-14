class RMQ:
    def __init__(self, nums):
        n = len(nums)
        self.N = int(log2(n)) + 1
        self.nums = nums

        rmq = [[0] * self.N for _ in range(n)]
        for i in range(n):
            rmq[i][0] = i

        j = 1
        while (1 << j) <= n:
            i = 0
            while i + (1 << j) -1 < n:
                l, r = rmq[i][j-1], rmq[i+(1<<(j-1))][j-1]
                if nums[l] >= nums[r]:
                    rmq[i][j] = l
                else:
                    rmq[i][j] = r
                i += 1
            j += 1

        self.rmq = rmq


    def min_q(self, l, r):
        j = int(log2(r - l + 1))
        ll, rr = self.rmq[l][j], self.rmq[r-(1<<j)+1][j]
        if self.nums[ll] >= self.nums[rr]:
            return ll
        return rr


def get_n(nums, take, rmq) -> List[int]:
    left, n = 0, len(nums)
    if take >= n:
        return nums

    ans = []
    for right in range(n-take, n):
        i = rmq.min_q(left, right)
        ans.append(nums[i])
        left = i + 1
    return ans


def merge(a, b) -> List[int]:
    a, b = deque(a), deque(b)
    ans = []
    while a and b:
        if a > b:
            ans.append(a.popleft())
        else:
            ans.append(b.popleft())
    if a:
        ans += list(a)
    if b:
        ans += list(b)
    return ans

class Solution:
    def maxNumber(self, A: List[int], B: List[int], k: int) -> List[int]:
        rmq_a, rmq_b = RMQ(A), RMQ(B)
        ans = [-100000000] * k
        for l in range(k+1):
            r = k - l
            arr_l = get_n(A, l, rmq_a)
            arr_r = get_n(B, r, rmq_b)

            tmp = merge(arr_l, arr_r)
            if len(tmp) == k:
                ans = max(ans, tmp)

        return ans
