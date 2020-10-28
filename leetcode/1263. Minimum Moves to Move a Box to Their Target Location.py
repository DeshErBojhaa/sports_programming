# 1263. Minimum Moves to Move a Box to Their Target Location
class Solution:
    def minPushBox(self, grid):
        N, M = len(grid), len(grid[0])
        S, B, T = None, None, None

        for i, r in enumerate(grid):
            for j, ch in enumerate(r):
                if ch == 'B':
                    B = (i, j)
                if ch == 'T':
                    T = (i, j)
                if ch == 'S':
                    S = (i, j)

        heap = []
        heappush(heap, (0, B, S))

        seen = set()

        while heap:
            move, box_cur, man_cur = heappop(heap)
            if box_cur == T:
                return move

            if (box_cur, man_cur) in seen:
                continue

            seen.add((box_cur, man_cur))

            for  (dx, dy) in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                man_nxt = (man_cur[0] + dx, man_cur[1] + dy)

                # Check if next position of the person is valid
                if not 0 <= man_nxt[0] < N or not 0 <= man_nxt[1] < M:
                    continue
                if grid[man_nxt[0]][man_nxt[1]] == '#':
                    continue
                if (box_cur, man_nxt) in seen:
                    continue

                # We push the box
                if man_nxt == box_cur:
                    box_nxt = (box_cur[0] + dx, box_cur[1] + dy)
                    if (not 0 <= box_nxt[0] < N or not 0 <= box_nxt[1] < M) or grid[box_nxt[0]][box_nxt[1]] == '#':
                        continue
                    if (box_nxt, man_nxt) in seen:
                        continue
                    heappush(heap, (move+1, box_nxt, man_nxt))
                else:
                    heappush(heap, (move, box_cur, man_nxt))

        return -1
