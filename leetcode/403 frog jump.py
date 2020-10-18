from functools import lru_cache
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        N = len(stones)
        if N == 1:
            return True
        if stones[1] > 1:
            return False
        d = {v:i for i, v in enumerate(stones)}
        
        @lru_cache(maxsize=None)
        def rec(cur, last_jump):
            # print(cur, last_jump)
            if cur == N-1:
                return True
            
            for next_jump in (last_jump-1, last_jump, last_jump+1):
                if next_jump <= 0:
                    continue
                next_stone = stones[cur] + next_jump
                if next_stone not in d:
                    continue
                if rec(d[next_stone], next_jump):
                    return True
            
            return False
        
        return rec(1, 1)
                
