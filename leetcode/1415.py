class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        
        def build(cur, last, st):
            if cur == n:
                ans.append(st)
                return
            
            for ch in 'abc':
                if ch == last:
                    continue
                build(cur+1, ch, st+ch)
        
        build(0, '', '')
        if k > len(ans):
            return ''
        return ans[k-1]
