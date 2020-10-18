class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def id_to_grid(ind):
            ind -= 1
            row = ind // n
            col = ind % n
            
            if row % 2:
                col = n - 1 - col
            
            row = n - 1 - row
            return row, col
        
        dist = {1:0}
        bfs = [1]
        
        for cur in bfs:
            for i in range(cur+1, cur+7):
                r, c = id_to_grid(i)
                if board[r][c] > -1:
                    i = board[r][c]
                if i == n * n:
                    return dist[cur] + 1
                if i not in dist:
                    dist[i] = dist[cur] + 1
                    bfs.append(i)
        return -1
