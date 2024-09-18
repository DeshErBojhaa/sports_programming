d = defaultdict(list)
    for i, v in enumerate(words):
        d[v].append(i)

    def ok(s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    ans = []
    if '' in d:
        for i, v in enumerate(words):
            if not ok(v):
                continue
            ans.extend(list(product(d[''], [i])))
            ans.extend(list(product([i], d[''])))

    for w, idx_1 in d.items():
        _w = w[::-1]
        for j in range(len(_w)):
            ww = _w[:j+1]
            if ww not in d:
                continue
            idx_2 = d[ww]
            if ok(ww + w):
                ans.extend(list(product(idx_2, idx_1)))
                # print('Cur:', w, '   ', ww, '+', w)
        for j in range(len(_w)-1, -1, -1):
            ww = _w[j:]
            if ww not in d:
                continue
            idx_2 = d[ww]
            if ok(w + ww):
                # print('Cur:', w, '   ', w, '+', ww)
                ans.extend(list(product(idx_1, idx_2)))

    ans2 = []
    seen = set()
    for v in ans:
        if v in seen:
            continue
        seen.add(v)
        if v[0] == v[1]:
            continue
        ans2.append([v[0], v[1]])

    return ans2
