import sys
from math import inf, isinf
from collections import defaultdict, deque
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
odd, even = [1,3,5,7,9], [0,2,4,6,8]
digits = []


def rec(cur, take_all):
    if cur == len(digits):
        return 1
    now = even if cur%2 else odd
    ans, rem_len = 0, len(digits) - cur
    for v in now:
        if not take_all and v > digits[cur]:
            break
        if not take_all and v == digits[cur]:
            ans += rec(cur+1, False)
        else:
            ans += 5**(rem_len - 1)
    return ans


def calc(num):
    global digits
    digits = list(map(int, str(num)))
    ans = sum(pow(5, i) for i in range(1, len(digits))) 
    for v in odd:
        if v > digits[0]:
            break
        ans += rec(1, v < digits[0])
    return ans


for tt in range(T):
    l, r = map(int, input().split())
    ans = calc(r) - calc(l-1)
    print(f'Case #{tt+1}: {ans}')

