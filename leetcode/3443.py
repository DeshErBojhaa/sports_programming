class Solution:
    def maxDistance(self, ss: str, k: int) -> int:
        oposit = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        def change(x, k):
            now = list(ss)
            for i, ch in enumerate(now):
                if ch in x and k:
                    k -= 1
                    now[i] = oposit[ch]
            return now
        # cnt = Counter(ss)
        # tup = {}
        # if cnt['N'] < cnt['S']:
        #     tup['N'] = cnt['N']
        # else:
        #     tup['S'] = cnt['S']
        # if cnt['E'] < cnt['W']:
        #     tup['E'] = cnt['E']
        # else:
        #     tup['W'] = cnt['W']
        
        # print(tup)
        # ss = list(ss)
        # for i, ch in enumerate(ss):
        #     if ch not in tup or k == 0 or tup[ch] == 0:
        #         continue
        #     op = oposit[ch]
        #     ss[i] = op
        #     tup[ch] -= 1
        #     k -= 1
        # print(ss)
        global_ans = 0
        for a in 'NS':
            for b in 'EW':
                sss = change(a+b, k)
                cnt, ans, dist = Counter(), 0, 0
                for s in sss:
                    _s = oposit[s]
                    if cnt[_s]:
                        cnt[_s] -= 1
                        dist -= 1
                    else:
                        cnt[s] += 1
                        dist += 1
                        ans = max(ans, dist)
                global_ans = max(global_ans, ans)
        return global_ans
