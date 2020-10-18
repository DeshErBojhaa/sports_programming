# 752. Open the Lock
from queue import SimpleQueue
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends, seen = set(deadends), set()
        q = SimpleQueue()
        if '0000' not in deadends:
            q.put(('0000', 0))
            seen.add('0000')
        
        def get_next(s):
            for i in range(4):
                val = int(s[i])
                for x in [val-1, val+1]:
                    if x >= 10:
                        x -= 10
                    elif x < 0:
                        x += 10
                    
                    yield s[:i] + str(x) + s[i+1:]
        
        while q.qsize():
            now, cost = q.get()
            if now == target:
                return cost
            
            for nxt in get_next(now):
                if nxt in seen or nxt in deadends:
                    continue
                q.put((nxt, cost + 1))
                seen.add(nxt)
        
        return -1



