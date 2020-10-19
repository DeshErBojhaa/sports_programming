from collections import Counter

def do():
    N = int(input())
    c = Counter()
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            c[i - min(i,j), j - min(i,j)] += row[j]
    
    return c.most_common(1)[0][1]


T = int(input())

for tt in range(1, T+1):
    ans = do()
    print('Case #{}: {}'.format(tt, ans))
