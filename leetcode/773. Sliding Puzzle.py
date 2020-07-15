# 773. Sliding Puzzle
from queue import SimpleQueue
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        endstate = tuple([tuple([1,2,3]),tuple([4,5,0])])
        q = SimpleQueue()
        q.put(tuple(map(tuple,board)))
        d = {}
        d[tuple(map(tuple,board))] = 0
        
        def genstate(s):
            s = list(map(list, s))
            for i in range(2):
                for j in range(3):
                    if s[i][j] != 0:
                        continue
                    for ni, nj in zip([i-1, i, i+1, i], [j, j+1, j, j-1]):
                        if ni < 0 or ni > 1 or nj < 0 or nj > 2:
                            continue
                        news = list(map(list, s))
                        news[ni][nj], news[i][j] = news[i][j], news[ni][nj]
                        yield tuple(map(tuple, news))
        
        
        while q.qsize():
            state = q.get()
            if state == endstate:
                return d[state]
            for nxtstate in genstate(state):
                if nxtstate == endstate:
                    return d[state] + 1
                if nxtstate in d:
                    continue
                d[nxtstate] = d[state] + 1
                q.put(nxtstate)
        
        return -1
            
