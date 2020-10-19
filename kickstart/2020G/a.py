from collections import *

T = int(input())

def do():
    s = input()
    N = len(s)
    kick, start = deque(), deque()

    for i in range(N):
        if s[i:i+4] == 'KICK':
            kick.append(i)
        if s[i:i+5] == 'START':
            start.append(i)
    
    ans = 0
    while kick and start:
        k = kick.popleft()
        while start and start[0] < k:
            start.popleft()
        ans += len(start)
    
    return ans

for tt in range(1, T+1):
    ans = do()
    print('Case #{}: {}'.format(tt, ans))