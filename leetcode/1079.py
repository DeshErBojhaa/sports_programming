class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        st = set()
        N = len(tiles)
        
        def rec(mask, s):
            st.add(s)
            if mask == 0:
                return
            
            for i in range(N):
                if mask & (1<<i) == 0:
                    continue
                mn = mask ^ (1 << i)
                rec(mn, s + tiles[i])
                rec(mn, s)
        
        rec((2**N)-1, '')
        # print(sorted(st))
        
        return len(st) - 1
