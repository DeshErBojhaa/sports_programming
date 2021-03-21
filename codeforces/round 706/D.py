from math import sqrt
from collections import Counter

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

n = int(input())
arr = list(map(int, input().split()))
asc, dsc = [1] * n, [1] * n
max_asc, max_dsc = -1, -1
for i in range(1, n):
    asc[i] = asc[i-1] + 1 if (arr[i-1] < arr[i]) else 1
    max_asc = max(max_asc, asc[i])

for i in range(n-2, -1, -1):
    dsc[i] = dsc[i+1] + 1 if (arr[i] > arr[i+1]) else 1
    max_dsc = max(max_dsc, dsc[i])

# print(asc, max_asc)
# print(dsc, max_dsc)
if max_dsc != max_asc or (max_asc % 2) == 0:
    print(0)
    exit(0)
cnt = 0
max_cnt = 0
for i in range(n):
    max_cnt += dsc[i] == max_dsc
    max_cnt += asc[i] == max_asc

    if asc[i] == dsc[i] == max_asc:
        cnt += 1

if cnt == 1 and max_cnt == 2:
    print(1)
else:
    print(0)
