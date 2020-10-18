    def findDuplicate(self, nums: List[int]) -> int:
        hear, tortoise = 0, 0
        while hear != tortoise or not hear:
            hear = nums[hear]
            tortoise = nums[nums[tortoise]]
        
        # print(hear, tortoise)
        hear = 0
        while hear != tortoise:
            hear = nums[hear]
            tortoise = nums[tortoise]
            # print('    ', hear, tortoise)
        return hear
