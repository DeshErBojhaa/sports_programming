import sys
from queue import SimpleQueue


def BFS(R, C):
    q = SimpleQueue()
    q.put((0, 0, 0, ''))

    while q.qsize():
        r, c, power, path = q.get()
        # print(r, c, pow(2, power), path)
        if r == R and c == C:
            return path
        move = pow(2, power)
        if move > 1e9:
            continue
        # 1. UP
        nr, nc = r + move, c
        if abs(nr) <= abs(R):
            q.put((nr, nc, power + 1, path + 'N'))

        # 2. DOWN
        nr, nc = r - move, c
        if abs(nr) <= abs(R):
            q.put((nr, nc, power + 1, path + 'S'))

        # 3. RIGHT
        nr, nc = r, c + move
        if abs(nc) <= abs(C):
            q.put((nr, nc, power + 1, path + 'E'))

        # 4. LEFT
        nr, nc = r, c - move
        if abs(nr) <= abs(C):
            q.put((nr, nc, power + 1, path + 'W'))

    return 'IMPOSSIBLE'


        Y, X = map(int, sys.stdin.readline().split())
        sys.stdout.write(f'Case #{t}: ')
        if (abs(X) + abs(Y)) % 2 == 0:
            sys.stdout.write('IMPOSSIBLE')
            continue
        ans = BFS(X, Y)
        sys.stdout.write(ans)
        sys.stdout.write("\n")
        sys.stdout.flush()

        var = (lambda x: [max(x - 2, x - 1), x])(bisect.bisect(list1, a, b, c))
