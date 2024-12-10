class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            return [True] * len(queries)
        
        c = Counter()
            
        true_count = [0]*(len(nums))
        
        for i in range(len(nums)-1):
            if nums[i]&1 != nums[i+1]&1:
                c += Counter([True])
            true_count[i+1] = c[True]

        ans = []
        print(true_count)
        for start,end in queries:
            if true_count[end] - true_count[start] == end-start:
                ans.append(True)
            else:
                ans.append(False)
            
        return ans        
