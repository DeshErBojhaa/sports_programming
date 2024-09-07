if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        unique, mx = set(), -1
        for _ in range(n):
            v = input().split()
            v = set(map(int, v[1:]))

            hand = 1

            for i in range(10**9):
                mx = max(mx, i)
                if i not in v:
                    hand -= 1
                    if hand < 0:
                        break

        x = min(m + 1, mx + 1)
        ans = x * mx
        if x <= m:
            ans += (m - x + 1) * (m + x) // 2
        print(ans)

