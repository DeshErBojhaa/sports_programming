def maxChunksToSorted(self, arr: List[int]) -> int:
        d, ans, mi = {v:i for i,v in enumerate(arr)}, 0, -1
        
        for i in range(len(arr)):
            mi = max(mi, d[i])
            ans += int(i == mi)
        
        return ans
