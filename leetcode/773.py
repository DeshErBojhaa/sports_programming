class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        solved = [[1,2,3],[4,5,0]]
        heap = [[0, tuple([tuple(x) for x in board])]]
        cost_dp = defaultdict(lambda : inf)
        cost_dp[heap[0][1]] = 0
        
        while heap:
            cost, now = heappop(heap)
            now = list(list(x) for x in now)
            if now == solved:
                return cost
            
            for i in range(2):
                for j in range(3):
                    if now[i][j] != 0:
                        continue
                    for ni, nj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                        if not 0 <= ni < 2 or not 0 <= nj < 3:
                            continue
                        
                        now[i][j], now[ni][nj] = now[ni][nj], now[i][j]
                        st = tuple([tuple(x) for x in now])
                        now[i][j], now[ni][nj] = now[ni][nj], now[i][j]
                        
                        if cost + 1 < cost_dp[st]:
                            cost_dp[st] = cost + 1
                            heappush(heap, [cost+1, st])
        
        return -1
