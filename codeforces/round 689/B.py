import sys
from itertools import accumulate
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
    r, c = map(int, input().split())
    arr = [None] * r
    pref = [[0]*c for _ in range(r)]

    for i in range(r):
        arr[i] = input()
        pref[i] = [1 if arr[i][j] == '*' else 0 for j in range(c)]
        pref[i] = list(accumulate(pref[i]))

    ans = 0

    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                continue
            for cur_row in range(i, r):
                relative_row = cur_row - i
                left, right = j - relative_row, j + relative_row
                # print(f'Left {left}   Right {right}    Relative {relative_row}')
                if not 0 <= left < c or not 0 <= right < c:
                    break
                star_cnt = pref[cur_row][right] - (pref[cur_row][left-1] if left - 1 >= 0 else 0)
                # print(f' row {cur_row}  Left Right  {left, right}   Cnt {star_cnt}')
                if star_cnt != (right - left + 1):
                    break
                ans += 1

    print(ans)
    # print()
