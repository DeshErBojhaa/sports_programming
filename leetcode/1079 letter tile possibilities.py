def numTilePossibilities(self, tiles: str) -> int:
        all_str, n = set(), len(tiles)
        
        @lru_cache(maxsize=None)
        def rec(mask, s):
            if bin(mask).count('1') == n:
                if s:
                    all_str.add(s)
                return
            
            for i in range(n):
                if (1<<i) & mask:
                    continue
                rec(mask | (1<<i), s)
                rec(mask | (1<<i), s+tiles[i])
        
        rec(0, '')
        #print(all_str)
        return len(all_str)
