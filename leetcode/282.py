class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def eval(ll):
            # print()
            # print("ll", ll)
            i, tmp = 0, []
            while i < len(ll):
                if ll[i] == '*':
                    tmp[-1] = tmp[-1] * ll[i+1]
                    i += 2
                    continue
                tmp.append(ll[i])
                i += 1
            last, sm = 0, 0
            # print(tmp)
            tmp = deque(tmp)
            while len(tmp) > 1:
                a, b, c = tmp.popleft(), tmp.popleft(), tmp.popleft()
                if b == '-':
                    tmp.appendleft(a - c)
                else:
                    tmp.appendleft(a + c)
                # print('   ', tmp)
            return tmp[-1] == target
        
        digits = list(int(x) for x in num)
        g_ans = []
        def rec(cur, ll):
            if cur == len(digits):
                nonlocal g_ans
                if eval(ll):
                    g_ans.append(''.join(map(str, ll)))
                return
            
            if len(ll) == 0:
                return rec(cur + 1, [digits[cur]])
            
            if ll and ll[-1] == '-' or ll[-1] == '+' or ll[-1] == '*':
                return rec(cur + 1, ll + [digits[cur]])

            if ll[-1] != '-' and ll[-1] != '+' and ll[-1] != '*':
                tmp_l = ll[:]
                if tmp_l[-1] != 0:
                    tmp_l[-1] *= 10
                    tmp_l[-1] += digits[cur]
                    rec(cur + 1, tmp_l)
                rec(cur, ll + ['+'])
                rec(cur, ll + ['-'])
                rec(cur, ll + ['*'])
            return
        
        rec(0, [])
        return sorted(g_ans)
