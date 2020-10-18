class Solution:
    def pourWater(self, h: List[int], V: int, K: int) -> List[int]:
        
        for i in range(V):  # Fall of i'th droplet
            resting_ind = None
            lowest_height = h[K]
            
            # Try to move left
            for li in range(K-1, -1, -1):
                if h[li] > lowest_height:
                    break
                if h[li] < lowest_height:
                    resting_ind = li
                    lowest_height = h[li]
            
            
            if resting_ind is not None:
                h[resting_ind] += 1
                continue
            
            resting_ind = K
            lowest_height = h[K]
            for ri in range(K+1, len(h)):
                if h[ri] > lowest_height:
                    break
                if h[ri] < lowest_height:
                    resting_ind = ri
                    lowest_height = h[ri]
            
            h[resting_ind] += 1
            
        return h
