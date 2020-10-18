class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        if len(s) == 1:
            return -1
        
        first_down = None
        for i in range(len(s)-2, -1, -1):
            if s[i] < s[i+1]:
                first_down = i
                break
            
        if first_down is None:
            return -1
        
        next_big_ind = first_down + 1
        for i in range(len(s)-1, -1, -1):
            if s[i] > s[first_down]:
                next_big_ind = i
                break
        
        s[first_down], s[next_big_ind] = s[next_big_ind], s[first_down]
        first_part = ''.join(s[:first_down+1])
        second_part = ''.join(sorted(s[first_down+1:]))

        # ss = s[:first_down] + s[first_down+1] + ''.join(sorted(s[first_down+2:] + s[first_down]))
        # print(first_part + second_part)
        val = int(first_part + second_part)
        return -1 if val > 2**31 else val
    
# 32345321
# 32353214

# 12443322
# 13222344
