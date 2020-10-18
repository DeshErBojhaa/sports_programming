from queue import SimpleQueue
class Solution:
    def updateMatrix(self, m: List[List[int]]) -> List[List[int]]:
        if not m:
            return []
        flag = set()
        R, C = len(m), len(m[0])
        Q = SimpleQueue()
        for i in range(R):
            for j in range(C):
                if m[i][j] == 0:
                    Q.put((i,j))
                    flag.add((i,j))
        
        while Q.qsize():
            i, j = Q.get()
            for r, c in zip([0,-1,0,1],[-1,0,1,0]):
                di, dj = i+r, j+c
                if di < 0 or di >= R or dj<0 or dj>=C or (di,dj) in flag:
                    continue
                m[di][dj] = m[i][j] + 1
                flag.add((di,dj))
                Q.put((di,dj))
        
        return m
