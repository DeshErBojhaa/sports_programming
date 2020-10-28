from collections import defaultdict, deque
from math import ceil
from sys import setrecursionlimit
import io, os


#  setrecursionlimit(300000)
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

T = int(input())

for tt in range(1, T+1):
    n = int(input())

    arr = list(map(int, input().split()))
    arr2 = arr[::-1]

    for i in range(len(arr)//2):
        arr2[i] *= -1

    print(*arr2)
