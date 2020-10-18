def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        
        for i in range(len(nums)):
            if i+1 == nums[i]:
                continue
            
            while i+1 != nums[i]:
                # print(i+1, nums[i], nums)
                ind = nums[i]
                if nums[ind-1] == ind:
                    ans.add(ind)
                    break
                nums[i], nums[ind-1] = nums[ind-1], nums[i]
                
        
        return list(ans)
