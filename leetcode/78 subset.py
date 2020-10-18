def subsets(self, nums: List[int]) -> List[List[int]]:
        s, n = set(), len(nums)
        
        def make__(cur, ans_t):
            if cur == n:
                s.add(ans_t)
                return
            
            make__(cur+1, ans_t + (nums[cur],))
            make__(cur+1, ans_t)
            
        make__(0, ())
        
        return list(s)
