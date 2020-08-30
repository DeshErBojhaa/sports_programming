# 1567. Maximum Length of Subarray With Positive Product
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        num_arr = []
        
        tmp = []
        for v in nums:
            if v == 0:
                num_arr.append(tmp)
                tmp = []
                continue
            tmp.append(v)
        
        if tmp:
            num_arr.append(tmp)
            
        ans = 0
        
        def find(arr):
            if not arr:
                return 0
            
            neg = sum(int(x<0) for x in arr)
            if neg % 2 == 0:
                return len(arr)
            ln = 0
            for i, v in enumerate(arr):
                if v < 0:
                    ln = max(ln, i, len(arr) - i - 1)
                    break
            
            for i in range(len(arr)-1,-1,-1):
                if arr[i] < 0:
                    ln = max(ln, len(arr) -i -1, i)
                    break
            
            return ln
        
        for arr in num_arr:
            f = find(arr)
            print(arr, f)
            ans = max(ans, f)
        
        return ans
