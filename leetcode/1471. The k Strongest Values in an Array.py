# 1471. The k Strongest Values in an Array
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        N, ans = len(arr), []
        arr.sort()
        median = arr[(N-1)//2]
        
        for v in arr:
            ans.append((abs(v - median), v))
        
        ans.sort(reverse=True, key=lambda x: (x[0],x[1]))
        
        return [x[1] for x in ans][:k]
