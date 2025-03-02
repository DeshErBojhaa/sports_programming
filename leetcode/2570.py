class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        s = {a:b for a, b in nums1}
        for i in range(len(nums2)):
            if nums2[i][0] not in s:
                s[nums2[i][0]] = nums2[i][1]
                continue
            s[nums2[i][0]] += nums2[i][1]
        
        return sorted([[a,b] for a, b in s.items()])
