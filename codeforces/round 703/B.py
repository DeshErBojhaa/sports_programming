import sys
from itertools import accumulate
import os
from io import BytesIO, IOBase
from math import ceil

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

for _ in range(T):
    n = int(input())
    x, y = [], []

    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    dis_x, dis_y = [], []

    for i in range(n):
        sm_x, sm_y = 0, 0
        for j in range(n):
            sm_x += abs(x[i] - x[j])
            sm_y += abs(y[i] - y[j])
        dis_x.append([sm_x, x[i]])
        dis_y.append([sm_y, y[i]])

    min_x, min_y = min(x[0] for x in dis_x), min(y[0] for y in dis_y)
    unique_x = set(x[1] for x in dis_x if x[0] == min_x)
    unique_y = set(y[1] for y in dis_y if y[0] == min_y)

    print(unique_x, unique_y)
    print(len(unique_x) * len(unique_y))
