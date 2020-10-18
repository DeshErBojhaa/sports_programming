def maxArea(self, h: List[int]) -> int:
        l, r, ans = 0, len(h)-1, 0
        
        while l < r:
            ans = max(ans, min(h[l],h[r])*(r-l))
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans
