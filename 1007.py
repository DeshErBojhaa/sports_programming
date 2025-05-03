class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = inf
        for tv in [1, 2, 3, 4, 5, 6]:
            up, down = 0, 0
            for i, t in enumerate(tops):
                if t == tv:
                    continue
                if bottoms[i] != tv:
                    up = inf
                    break
                up += 1
            
            for i, t in enumerate(bottoms):
                if t == tv:
                    continue
                if tops[i] != tv:
                    down = inf
                    break
                down += 1
            ans = min(ans, min(up, down))
        return ans if ans < inf else -1
