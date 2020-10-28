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

from math import inf 
from heapq import heappush, heappop
# from sys import setrecursionlimit
# setrecursionlimit(300000)

N = int(input())
display, store, sold, out_of_store = [], list(range(1, N+1)), [False] * (N+1), [False] * (N+1)
ans = []

for i in range(2*N):
    inp = input()
    if inp[0] == '+':
        print(inp)
        while store and out_of_store[store[-1]]:
            store.pop()
        if not store:
            break
        heappush(display, store.pop())
        out_of_store[display[0]] = True
        ans.append(display[0])
        sold[display[0]] = True

        print('Display', display)
        print('Store', store)
        print('Ans', ans)
    else:
        _, num = inp.split()
        num = int(num)
        print(inp)
        from_display = heappop(display)

        if num >= from_display:
            if not sold[num]:
                break
            sold[num] = True
            out_of_store[num] = True
            while store and out_of_store[store[-1]]:
                store.pop()
        elif num < from_display:
            sold[num] = True
            out_of_store[num] = True
            while store and out_of_store[store[-1]]:
                store.pop()
            out_of_store[from_display] = False
            store.append(from_display)

            if ans[-1] == from_display:
                sold[from_display] = False
                ans.pop()

            ans.append(num)

        print('Display', display)
        print('Store', store)
        print('Ans', ans)
        

print('Display', display)
print('Store', store)
print('Ans', ans)
while store and sold[store[-1]]:
    store.pop()
if display or store:
    print('NO')
else:
    print('YES')
    print(*ans)



# 3 10 9 7 1 8 5 4 6 2 



