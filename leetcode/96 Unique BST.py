ans = [1,1,2,5,14,42,132]
class Solution:
    def numTrees(self, n: int) -> int:
        
        def calc(nn):
            if nn < len(ans):
                return ans[nn]
            x = 0
            for i in range(1,nn+1):
                l = calc(i-1)
                r = calc(nn - i)
                
                #print(i, nn-i,  '      ', l*r)
                x += l*r
            while len(ans) <= nn:
                ans.append(0)
            ans[nn] = x
            return x
        
        return calc(n)
