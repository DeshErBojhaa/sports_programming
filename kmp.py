ss = 'abcdefghijklmnopqrstuvwxyz'+ '#' + s
N, k = len(ss), 0
par = [0] * N

for i in range(1, N):
    while k > 0 and ss[i] != ss[k]:
        k = par[k-1]
    k += ss[i] == ss[k]
    par[i] = k