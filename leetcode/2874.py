class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pref, mv, ans = 0, -1010100101, 0
        for n in nums:
            ans = max(ans, pref * n)
            pref = max(pref, mv - n)
            mv = max(mv, n)
        return ans
