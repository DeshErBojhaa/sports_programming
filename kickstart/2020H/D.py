import sys
from math import inf, isinf
from collections import defaultdict, deque
import os
from io import BytesIO, IOBase

#Fast IO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

T = int(input())

def bfs(a, b, name_id, id_name, char_names):
    q = deque([a])
    seen_ch = set()
    dist = defaultdict(lambda: inf)
    dist[a] = 0

    while q:
        now = q.popleft()
        if now == b:
            return dist[now]
        cur_name = id_name[now]
        for ch in cur_name:
            if ch in seen_ch:
                continue
            seen_ch.add(ch)
            for nxt in char_names[ch]:
                if dist[nxt] > dist[now] + 1:
                    q.append(nxt)
                    dist[nxt] = dist[now] + 1

    return -1 if isinf(dist[b]) else dist[b]


for tt in range(T):
    N ,Q = map(int, input().split())
    names = input().split()
    name_id = {n:i+1 for i, n in enumerate(names)}
    id_name = {i+1:n for i, n in enumerate(names)}

    dd = defaultdict(set)

    for n in names:
        nid = name_id[n]
        for ch in n:
            dd[ch].add(nid)
    
    ans = []
    for qq in range(Q):
        a, b = map(int, input().split())
        ans.append(bfs(a, b, name_id, id_name, dd))
    
    for i, v in enumerate(ans):
        if v > 0:
            ans[i] += 1

    print(f'Case #{tt+1}: ', end='')
    print(*ans)
