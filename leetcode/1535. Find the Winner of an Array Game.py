# 1535. Find the Winner of an Array Game
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        candidate, cnt = arr[0], 0
        
        for x in arr[1:]:
            if x > candidate:
                candidate = x
                cnt = 0

            cnt += 1
            if cnt == k:
                break
        
        return candidate
            
