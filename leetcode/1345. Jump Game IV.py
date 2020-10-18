from collections import defaultdict
from queue import SimpleQueue
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        same_val, N = defaultdict(list), len(arr)
        flag = [float('inf')] * N
        
        for i, v in enumerate(arr):
            same_val[v].append(i)
        
        q = SimpleQueue()
        q.put(0)
        flag[0] = 0
        
        while q.qsize():
            if flag[N-1] < float('inf'):
                return flag[N-1]
            top = q.get()
            # print(top)
            if top - 1 > 0 and flag[top] + 1 < flag[top - 1]:
                flag[top - 1] = flag[top] + 1
                q.put(top-1)
            if top + 1 < N and flag[top] + 1 < flag[top + 1]:
                flag[top + 1] = flag[top] + 1
                q.put(top + 1)
            
            for nxt in same_val[arr[top]]:
                if flag[top] + 1 < flag[nxt]:
                    flag[nxt] = flag[top] + 1
                    q.put(nxt)
            del same_val[arr[top]]
            
        return flag[N-1]
