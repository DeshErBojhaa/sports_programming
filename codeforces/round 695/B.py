import sys
from collections import Counter
from math import ceil
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

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0

    for i in range(1, n-1):
        if arr[i-1] < arr[i] > arr[i+1] or arr[i-1] > arr[i] < arr[i+1]:
            total += 1
    
    def is_danger(idx):
        if idx <= 0 or idx >= n-1:
            return False
        return arr[idx-1] < arr[idx] > arr[idx+1] or arr[idx-1] > arr[idx] < arr[idx+1]

    mx_reduce = 1
    for i in range(1, n-1):
        if arr[i-1] < arr[i] > arr[i+1] or arr[i-1] > arr[i] < arr[i+1]:
            a, p, nx = arr[i], arr[i-1], arr[i+1]
            prev_danger = is_danger(i-1)
            next_danger = is_danger(i+1)
            now = prev_danger + next_danger + 1
            # Make eq with prev
            arr[i] = p
            prev_danger = is_danger(i-1)
            next_danger = is_danger(i+1)

            prv = prev_danger + next_danger
            
            # Make equal with next
            arr[i] = nx

            prev_danger = is_danger(i-1)
            next_danger = is_danger(i+1)

            nxt = prev_danger + next_danger
            
            reduce = now - min(prv, nxt)

            arr[i] = a
            mx_reduce = max(mx_reduce, reduce)
    
    print(max(0, total - mx_reduce))

