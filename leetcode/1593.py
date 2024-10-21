class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans, N = 0, len(s)
        def rec(cur, st):
            if cur == N:
                nonlocal ans
                ans = max(ans, len(st))
                return
            
            for i in range(cur + 1, N+1):
                tmp = s[cur: i]
                if tmp in st:
                    continue
                st.add(tmp)
                rec(i, st)
                if tmp in st:
                    st.remove(tmp)
        
        rec(0, set())
        return ans
