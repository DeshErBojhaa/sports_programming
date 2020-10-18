from queue import PriorityQueue
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        # Also can be done with a BFS like algo + Priority queue
        par = {}
        start, end = (0,0), (len(A)-1, len(A[0])-1)
        joinet_set = set()
        values = PriorityQueue()
        for i, r in enumerate(A):
            for j, v in enumerate(r):
                par[(i,j)] = (i,j)
                values.put((-v,i,j))
                
        def find_parent(t):
            while par[t] != t:
                t = par[t]
            return par[t]
        
        ans = float('inf')
        while values.qsize():
            v, r, c = values.get()
            v = -v
            # print('>', r,c,v)    
            for i, j in zip([0,-1,0,1], [-1,0,1,0]):
                nr, nc = r+i, c+j
                if (nr,nc) in joinet_set:
                    # print('>> ', nr, nc, 'par[', find_parent((r,c)), '] = ', find_parent((nr,nc)))
                    par[find_parent((r,c))] = find_parent((nr,nc))
                    # break
            joinet_set.add((r,c))
            ans = min(ans, v)
            if find_parent(start) == find_parent(end):
                break
        return ans
            
        
