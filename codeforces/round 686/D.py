from math import sqrt
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

lim = 100010
prime = [True] * lim
prime[0] = prime[1] = False

for i in range(2, int(sqrt(lim)) + 2):
    if not prime[i]:
        continue
    for j in range(i * i, lim, i):
        prime[j] = False

primes = []
for i in range(2, lim):
    if prime[i]:
        primes.append(i)


T = int(input())

for _ in range(T):
    nn = int(input())
    main_ans = [1]

    for p in primes:
        n = nn
        ans = [1]
        while n % p == 0 and p % ans[-1] == 0 and (n//p) % p == 0:
            ans.append(p)
            n //= p
    
        if n > 1:
            ans.append(n)
        if len(ans) > len(main_ans):
            main_ans = ans

    print(len(main_ans) -1)
    print(*main_ans[1:])
