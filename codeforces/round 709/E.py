import sys
import sys
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
from heapq import heappop, heappush

n = int(input())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
arr = lsit(B)
minheap_pos, minheap_neg = [], []

for i, (h, b) in enumerate(zip(H, B)):
    if b >= 0:
        heappush(minheap_pos, [h, b, i])
    else:
        heappush(minheap_neg, [-b, h, i])

while minheap_pos:
    h, b, start_idx = heappop(minheap_pos)
    for i in range(start_idx + 1, n):
        if arr[i] >= 0:
            break
        arr[i] = 0

    for i in range(start_idx-1, -1, -1):
        if arr[i] >= 0:
            break
        arr[i] = 0

while minheap_neg:
    b, h, start_idx = heappop(minheap_neg)
    b = -b
    for i in range(start_idx + 1, n):
        if arr[i] >= 0:
            break
        if arr[i] > b:
            break
        


