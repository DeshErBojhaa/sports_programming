class Solution:
    def stableMountains(self, height: List[int], th: int) -> List[int]:
        ans = []
        for i, v in enumerate(height[1:], 1):
            if height[i-1] > th:
                ans.append(i)
        
        return ans
