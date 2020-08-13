# 1286. Iterator for Combination
from collections import deque
class CombinationIterator:

    def __init__(self, S: str, cl: int):
        self.q = deque()
        N = len(S)
        
        def rec(cur, l):
            if cur == N:
                if len(l) == cl:
                    self.q.append(''.join(l))
                return
            if len(l) == cl:
                self.q.append(''.join(l))
                return
            if len(self.q) > 10000:
                return
            rec(cur+1, l + [S[cur]])
            rec(cur+1, l)
        
        rec(0, [])

    def next(self) -> str:
        # print(self.q)
        return self.q.popleft()

    def hasNext(self) -> bool:
        return len(self.q)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
