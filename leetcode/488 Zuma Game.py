class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = ''.join(sorted(hand))
        q = deque([[board, hand]])
        seen = {board + '#' + hand}

        @cache
        def collaps(ss):
            ss = list(ss)
            while True:
                brk = True
                s = []
                groups = [list(g) for _, g in groupby(ss)]
                for g in groups:
                    if len(g) >= 3:
                        brk = False
                        continue
                    s.extend(g)
                ss = s
                if brk:
                    break
            # ss = list(chain.from_iterable(ss))
            return ''.join(ss)


        while q:
            b, h = q.popleft()
            for i, ch in enumerate(h):
                if i and h[i-1] == ch:
                    continue
                for j in range(len(b) + 1):
                    if j and b[j-1] == ch:
                        continue
                    pick = False
                    if j < len(b) and b[j] == ch:
                        pick = True
                    if 0 < j < len(b) and b[j-1] == b[j] and b[j] != ch:
                        pick = True
                    if pick:
                        nb = collaps(b[:j] + ch + b[j:])
                        if nb == "":
                            return len(hand) - len(h) + 1
                        nh = h[:i] + h[i+1:]
                        tmp = nb + '#' + nh
                        if tmp in seen:
                            continue
                        seen.add(tmp)
                        q.append([nb, nh])
        return -1
