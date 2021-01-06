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


N = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
max_binary_len = len(bin(max_val)) - 2

class Node:
    def __init__(self):
        self.zero = None
        self.one = None
        self.end = False

root = Node()

for v in arr:
    cur = root
    ln = max_binary_len - 1

    while ln >= 0:
        msb = (v & (1<<ln)) > 0
        if msb:
            if cur.one is None:
                cur.one = Node()
            cur = cur.one
        else:
            if cur.zero is None:
                cur.zero = Node()
            cur = cur.zero
        ln -= 1
    cur.end = 1


def rec(cur):
    if not cur:
        return 0
    if cur.end:
        return cur.end

    left = rec(cur.zero)
    right = rec(cur.one)

    if left > 1 and right > 1:
        return 1 + max(left, right)
    
    return left + right


valid = rec(root)
print(N - valid)
