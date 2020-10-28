from collections import defaultdict, deque
from math import ceil
from sys import setrecursionlimit
import io, os


setrecursionlimit(300000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())

par = [-1] + list(map(int, input().split()))
_g = defaultdict(list)
real_leaves = set(range(n))

people = list(map(int, input().split()))
children = [0] * (n+1)

for i, v in enumerate(par):
    real_leaves.discard(v-1)
    _g[i].append(v-1)
    children[v-1] += 1


q = deque(real_leaves)
leaves, people_cnt = [0] * (n+1), people[:]

for i in real_leaves:
    leaves[i] = 1

ans = 0

while True:
    q2 = deque()
    while q:
        now = q.popleft()
        ans = max(ans, ceil(people_cnt[now] / leaves[now]))

        for par in _g[now]:
            leaves[par] += leaves[now]
            people_cnt[par] += people_cnt[now]
            children[par] -= 1

            if children[par] == 0:
                q2.append(par)

    if not q2:
        break
    q = q2
print(ans)
