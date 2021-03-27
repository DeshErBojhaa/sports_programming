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
    arr = list(map(int, input().split()))
    diff_set = set((b-a) for a, b in zip(arr, arr[1:]))

    if len(diff_set) <= 1:
        print(0)
        continue

    if len(diff_set) > 2:
        print(-1)
        continue
    
    mod_val = sum(abs(x) for x in diff_set)
    inc = max(diff_set)
    dec = min(diff_set)
    if dec >= 0 :
        print(-1)
        continue

    if arr[0] >= mod_val:
        print(-1)
        continue

    valid = True
    last = arr[0]
    for i in range(1, n):
        now_val = (last + inc) % mod_val
        if now_val != arr[i]:
            valid = False
            break
        last = now_val

    if valid:
        print(mod_val, inc)
    else:
        print(-1)
    
    
