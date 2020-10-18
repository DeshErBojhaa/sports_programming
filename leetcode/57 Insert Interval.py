# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        ans = []
        ivstart, ivend = float('inf'), float('-inf')
        
        for iv in intervals:
            if iv[1] < ni[0] or iv[0] > ni[1]:
                ans.append(iv)
                continue
            
            ivstart = min(ivstart, iv[0], ni[0])
            ivend = max(ivend, iv[1], ni[1])
        
        # New Interval overlapped with some interval
        if ivend > 0:
            ans.append([ivstart, ivend])
        else:
            ans = intervals + [ni]
            
        ans.sort()
        return ans
