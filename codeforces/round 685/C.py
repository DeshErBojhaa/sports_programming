import sys
import os
from io import BytesIO, IOBase
from math import inf
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
    N, K = map(int, input().split())

    a = input()
    b = input()
    ca, cb = Counter(a), Counter(b)

    last = b[0]
    cnt = 1
    ok = True

    for i, ch in enumerate(b[1:], 1):
        if ch != last:
            extra = cnt % K
            cb[last] -= extra
            ca[last] -= extra
            if ca[last] < 0:
                ok = False
                break
            if ca[last] == 0:
                del ca[last]
            if cb[last] == 0:
                del cb[last]

            last = ch
            cnt = 1
        else:
            cnt += 1

    # print(1, ca, cb, ok)
    if not ok:
        print('NO')
        continue

    if cnt > 0:
        extra = cnt%K
        cb[last] -= extra
        ca[last] -= extra

        if ca[last] < 0:
            print('NO')
            continue
        if ca[last] == 0:
            del ca[last]
    
    # print(2, ca, cb, ok)

    for ch_b in sorted(cb):
        cnt_b = cb[ch_b]
        if cnt_b == 0:
            continue

        for ch_a in sorted(ca):
            cnt_b = cb[ch_b]
            # print(f'a {ch_a}:{ca[ch_a]}   b {ch_b}:{cb[ch_b]}')
            if ch_a > ch_b:
                ok = False
                break
            cnt_a = ca[ch_a]
            if cnt_a%K != 0:
                ok = False
                break
            mn = min(cnt_a, cnt_b)
            cb[ch_b] -= mn
            ca[ch_a] -= mn

            if ca[ch_a] < 0:
                ok = False
                break
            if ca[ch_a] == 0:
                del ca[ch_a]
            if cb[ch_b] == 0:
                break

    if ok:
        print('YES')
    else:
        print('NO')

