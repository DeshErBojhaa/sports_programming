def trap(self, h: List[int]) -> int:
        ans, st = 0, []
        
        for i, v in enumerate(h):
            if not st or h[st[-1]] >= v:
                st.append(i)
                continue
            
            tmpans, ch = 0, 0
            while st and h[st[-1]] < v:
                x = (min(v, h[st[-1]]) - ch) * (i - st[-1] -1)
                tmpans += x
                ch = h[st.pop()]
            
            ans += tmpans
            if st:
                x = (min(v, h[st[-1]]) - ch) * (i - st[-1] -1)    
                ans += x
                if h[st[-1]] == v:
                    st.pop()
            
            st.append(i)

        return ans
