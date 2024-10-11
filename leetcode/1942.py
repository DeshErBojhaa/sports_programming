class Solution:
    def smallestChair(self, times: List[List[int]], xxx: int) -> int:
        arr, pos, n = [], dict(), len(times)
        for i, (a, b) in enumerate(times):
            arr.append([a, 1, i])
            arr.append([b, -1, i])
        arr.sort()
        
        chairs = list(range(n))
        heapify(chairs)
    
        for tm, sgn, i in arr:
            if sgn == -1:
                chair = pos[i]
                del pos[i]
                heappush(chairs, chair)
                continue
            chair = heappop(chairs)
            if i == xxx:
                return chair
            pos[i] = chair
        return n-1
