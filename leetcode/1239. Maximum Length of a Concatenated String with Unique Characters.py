# 1239. Maximum Length of a Concatenated String with Unique Characters
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        
        for a in arr:
            set_a = set(a)
            if len(set_a) != len(a):
                continue
            for s in dp:
                if not set_a.isdisjoint(s):
                    continue
                dp.append(s|set_a)
        
        return max(len(s) for s in dp)
