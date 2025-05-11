class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for x in arr:
            if x % 2 == 0:
                cnt = 0
                continue
            cnt += 1
            if cnt == 3:
                return True
        return False
