import sys
from collections import defaultdict
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




def cs(n):
    valid = 1
    depth = 0
    ans = [-1] * ((2*n)-1)
    def build(rem, arr):
        nonlocal depth
        depth += 1
        if not rem:
            nonlocal valid, ans
            if valid == 1:
                print(arr)
                valid = 0
            ans = max(ans, arr)
            return

        for i in range((2*n) - 1):
            if arr[i] > - 10:
                continue

            for j in range(len(rem)):
                v = rem[j]
                if i + v >= len(arr):
                    continue
                if arr[i + v] > -10:
                    continue

                if v == 1:
                    arr[i] = v
                else:
                    arr[i] = arr[i + v] = v
    
                rem.pop(j)
                build(rem, arr)
                if v == 1:
                    arr[i] = -100
                else:
                    arr[i] = arr[i + v] = -100
                rem.insert(j, v)

    r = list(range(1, n+1))
    init = [-100] * ((2 * n) - 1)
    build(r[::-1], init)
    print(ans)
cs(8)
