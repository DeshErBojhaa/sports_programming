class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mxind = -1
        d = {ch:i for i, ch in enumerate(S)}
        ln, ans = 1, []
        
        for i, ch in enumerate(S):
            mxind = max(mxind, d[ch])
            if i == mxind:
                ans.append(ln)
                ln = 1
            else:
                ln += 1
        
        return ans
