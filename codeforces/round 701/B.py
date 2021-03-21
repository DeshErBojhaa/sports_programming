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


n, q, k = map(int, input().split())
aux = [0] * n
arr = list(map(int, input().split()))

for i, v in enumerate(arr):
    if not i:
        left = 0
    else:
        left = arr[i-1]
    if i + 1 < n:
        right = arr[i+1]
    else:
        right = k + 1

    aux[i] = right - left - 2

acc = list(accumulate(aux))
for _ in range(q):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if a == b:
        print(k-1)
        continue
    aa, bb, ans = a + 1, b - 1, 0
    left_extreme = arr[a] - 1
    left_right = arr[a + 1] - arr[a] - 1

    right_extreme = k - arr[b]
    right_left = arr[b] - arr[b-1] - 1
    mid = 0
    if b - a >= 2:
        mid = acc[bb] - acc[aa-1]

    ans = left_extreme + left_right + mid + right_left + right_extreme
    # print(left_extreme, left_right, mid, right_left, right_extreme)
    print(ans)

