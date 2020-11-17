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

for tt in range(T):
    N, Q = map(int, input().split())
    names = input().split()
    
    dp = [[inf] * 26 for _ in range(26)]
    name_id = {}

    for i, n in enumerate(names, 1):
        name_id[i] = n
        for j, ch in enumerate(n):
            for k, ch2 in enumerate(n):
                dp[ord(ch) - ord('A')][ord(ch2) - ord('A')] = 1
    
    for i in range(26):
        dp[i][i] = 0
    #for r in dp:
    #    print(r)
    #print()
    for k in range(26):
        for i in range(26):
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    ans = []
    for _ in range(Q):
        a, b = map(int, input().split())
        a, b = name_id[a], name_id[b]
        val = inf
        for ch in a:
            for ch2 in b:
                val = min(val, dp[ord(ch) - ord('A')][ord(ch2) - ord('A')])
        ans.append(-1 if isinf(val) else val+2)

    print(f'Case #{tt+1}: ', end='')
    print(*ans)

