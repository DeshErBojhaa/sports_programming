import sys
from math import inf, ceil


import os
from io import BytesIO, IOBase
from collections import Counter

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
    arival_departure, delay = [], []
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        arival_departure.append([a, b])
    delay = list(map(int, input().split()))

    tt, from_last, last_departure = 0, arival_departure[0][0], 0
    ans = None
    for i in range(n):
        if i:
            from_last = arival_departure[i][0] - arival_departure[i-1][1]
        
        extra = delay[i] + from_last
        arrival = last_departure + extra
        tt = max(tt, delay[i] + from_last + last_departure)
        if i == n-1:
            ans = arrival
        # print(f'Arived {i + 1} th station at {arrival}')
        stay = ceil((arival_departure[i][1] - arival_departure[i][0])/2)
        departure = max(arrival + stay, arival_departure[i][1])
        # print(f'Left {i+1} th station at {departure}')
        last_departure = departure

    print(ans)
