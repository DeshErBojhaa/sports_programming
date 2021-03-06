from collections import deque

from math import inf, sqrt, ceil

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

T = int(input())

for _ in range(T):
    friend, days = map(int, input().split())
    avail_friends = [None] * days
    lim = ceil(days / 2)
    rem = [lim] * (friend + 1)
    for i in range(days):
        tmp = list(map(int, input().split()))
        avail_friends[i] = [i] + tmp[1:]
    
    avail_friends.sort(key=lambda x: len(x))
    path = [None] * days

    for on_day in avail_friends:
        day_idx = on_day[0]
        max_rem = -inf
        friend_idx = None

        for fi in on_day[1:]:
            if rem[fi] > 0 and rem[fi] > max_rem:
                max_rem = rem[fi]
                friend_idx = fi

        if friend_idx is None:
            path = None
            break

        path[day_idx] = friend_idx
        rem[friend_idx] -= 1

    if path is None:
        print('NO')
        continue

    print('YES')
    print(*path)
        

