    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        #print(nums)
        cnt = 0
        mid = 0
        while hi > lo:
            cnt += 1
            #if cnt > 6:
            #    break
            mid = (hi+lo)//2
            # print(lo, mid, hi)
            if mid%2:
                if nums[mid+1] > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
                continue
            
            if nums[mid+1] > nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        print(lo, hi, mid)
        return nums[hi]
