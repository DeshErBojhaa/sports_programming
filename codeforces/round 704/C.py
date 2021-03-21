
from math import inf
import sys
import os
from io import BytesIO, IOBase
from collections import defaultdict

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
from collections import Counter


n, m = map(int, input().split())
a = input()
b = input()

left, right = [None] * m, [None] * m

idx_a = 0
for i, ch in enumerate(b):
    while a[idx_a] != ch:
        idx_a += 1
    if ch == a[idx_a]:
        left[i] = idx_a
        idx_a += 1

idx_a = n - 1
for i in range(m-1, -1, -1):
    ch = b[i]
    while a[idx_a] != ch:
        idx_a -= 1
    if ch == a[idx_a]:
        right[i] = idx_a
        idx_a -= 1


ans = 1

for i in range(1, m):
    ans = max(ans, right[i] - left[i-1])

print(ans)


