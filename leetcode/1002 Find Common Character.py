class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        
        for c in set(A[0]):
            cnt = A[0].count(c)
            for st in A[1:]:
                cnt = min(cnt, st.count(c))
            ans.extend(list(c*cnt))
        
        return ans
