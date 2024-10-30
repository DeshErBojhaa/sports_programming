class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def lis(arr):
            l, iii = [arr[0]], 0
            ll = [1] * len(arr)
            for a in arr[1:]:
                iii += 1
                idx = bisect_left(l, a)
                if len(l) == idx:
                    l.append(a)
                l[idx] = a
                ll[iii] = len(l)
            # print(arr, '=>', len(l))
            return ll
        
        ans = len(nums)
        l = lis(nums)
        r = lis(nums[::-1])[::-1]
        
        for i in range(1, len(nums)-1):
            if l[i] < 2 or r[i] < 2:
                continue
            sm = l[i] + r[i] - 1
            ans = min(ans, len(nums) - sm)
        
        return ans
