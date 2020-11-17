from collections import deque, defaultdict
from math import inf
from sys import setrecursionlimit
import sys
import os
from io import BytesIO, IOBase
from random import shuffle


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


# setrecursionlimit(300000)


def accepted(N, arr):
    levels = [1]

    last_num, node_chunk, height= -inf, 0, 0
    for i in range(1, N):
        v = arr[i]
        if v < last_num:
            node_chunk += 1
            if node_chunk == levels[height]:
                height += 1
                node_chunk = 0

        if height + 1 >= len(levels):
            levels.append(0)

        levels[height + 1] += 1
        last_num = v

    return len(levels) - 1


def wrong(N, arr):
    levels = [1]

    i = 1
    last_num, node_chunk, level_nodes = -inf, 0, 0
    while i < N:
        for j in range(i, N):
            if arr[j] < last_num:
                node_chunk += 1
                last_num = arr[j]
                if node_chunk >= levels[-1]:
                    levels.append(level_nodes)
                    last_num = arr[j]
                    node_chunk = 0
                    level_nodes = 1
                    break
                level_nodes += 1
            else:
                level_nodes += 1
                last_num = arr[j]
        i = j + 1

    levels.append(level_nodes)
    return len(levels) - 1


# wrong(8, [1,7,6,8,3,5,4,2])
arr = list(range(2, 12))
for i in range(1000):
    shuffle(arr)
    n = len(arr) + 1
    if accepted(n, [1] + arr) == wrong(n, [1] + arr):
        print('Ok')
        continue
    print([1] + arr, accepted(n, [1] + arr), wrong(n, [1] + arr))
