class Solution:
    def minAreaRect(self, p: List[List[int]]) -> int:
        if len(p) < 4:
            return 0
        
        p = sorted(p)
        s = set((i,j) for i,j in p)
        
        ans = float('inf')
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                bottom_left, top_right = p[i], p[j]
                l, h = abs(bottom_left[0]-top_right[0]), abs(bottom_left[1]-top_right[1])
                if not l or not h:
                    continue
                if l * h > ans:
                    continue
                if (top_right[0], bottom_left[1]) in s and (bottom_left[0], top_right[1]) in s:
                    
                    # print(a,c, '     ', l, h)
                    ans = min(ans, l * h)
        
        return 0 if ans==float('inf') else ans
                
        
