
import os, sys
from io import BytesIO, IOBase
from types import GeneratorType
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
import math, string
import heapq as h, time
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
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

def get_min_idx(arr, n, start):
    mv, idx = float('inf'), start
    for i in range(start, n):
        if arr[i] < mv:
            mv = arr[i]
            idx = i
    return idx

def get_score(arr, n):
    ans = 0

    for i in range(n-1):
        j = get_min_idx(arr, n, i)
        ans += (j - i + 1)
        arr[i:j+1] = arr[i:j+1][::-1]
    return ans

all_res = defaultdict(lambda: 'IMPOSSIBLE')

def rec(mask, arr, n):
    if mask == ((1<<n)-1):
        sc = get_score(list(arr), n)
        if (n, sc) not in all_res:
            all_res[n, sc] = ' '.join(map(str, arr))
        return

    for i in range(n):
        if mask & (1<<i) != 0:
            continue
        nmask = mask ^ (1 << i)
        rec(nmask, arr + [i+1], n)

for i in range(2, 8):
    rec(0, [], i)

def solve():
    n, tot = map(int, input().split())
    return all_res[n, tot]

        
for _ in range(int(input())):
    print("Case #{}: {}".format(_+1, solve()))
