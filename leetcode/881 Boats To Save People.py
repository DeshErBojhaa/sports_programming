class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = sorted(people, reverse=True)
        l, h = 0, len(p) -1
        ans = 0

        while l <= h:
            if l<h and p[l] + p[h] <= limit:
                h -= 1
            l += 1
            ans += 1
        
        return ans
