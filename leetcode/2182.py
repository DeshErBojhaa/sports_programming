class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        arr = deque(sorted(s, reverse=True))
        ans, tmp, cum, last = [], deque(), 0, ''

        while arr:
            if tmp and cum + (tmp[0] == last) <= repeatLimit:
                ans.append(tmp.popleft())
                cum = cum + 1 if int(ans[-1] == last) else 1
                last = ans[-1]
                continue
            now = arr.popleft()
            if cum + (now == last) > repeatLimit:
                tmp.append(now)
                continue

            ans.append(now)
            cum = cum + 1 if int(now == last) else 1
            last = now
        while tmp and cum + (tmp[0] == last) <= repeatLimit:
            ans.append(tmp.popleft())
            cum = cum + 1 if int(ans[-1] == last) else 1
            last = ans[-1]
        return ''.join(ans)
