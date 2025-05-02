class Solution:
    def pushDominoes(self, dd: str) -> str:
        N = len(dd)
        lbound, ans = -1, list(dd)
        rr = deque()

        for i, ch in enumerate(dd):
            if ch == 'R':
                if rr:
                    r = rr.popleft()
                    for x in range(r+1, i):
                        ans[x] = 'R'
                
                rr.append(i)
                lbound = i
            elif ch == 'L':
                if rr:
                    r = rr.popleft()
                    l = i
                    while r < l:
                        ans[r] = 'R'
                        ans[l] = 'L'
                        r += 1
                        l -= 1
                else:
                    for x in range(lbound+1, i):
                        ans[x] = 'L'
                lbound = i
        if rr:
            for i in range(rr[0], N):
                ans[i] = 'R'
        return ''.join(ans)
