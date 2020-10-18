# 726. Number of Atoms
class Solution:
    def countOfAtoms(self, formula):
        def rec(s, factor):
            c = Counter()
            var, cnt = '', 0
            i = 0
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    cnt = (cnt * 10) + int(ch)
                if ch.isupper():
                    if var:
                        c[var] += max(1, cnt)
                    cnt = 0
                    var = ch
                if ch.islower():
                    var += ch
                if ch == '(':
                    c[var] += max(1, cnt)
                    cnt = 0
                    var = ''
                    subformula, bal, mul = '', 1, ''
                    for j in range(i+1, len(s)):
                        if s[j] == ')':
                            bal -= 1
                            if bal:
                                subformula += s[j]
                        elif s[j] == '(':
                            bal += 1
                            subformula += s[j]
                        else:
                            subformula += s[j]
                        if bal == 0:
                            k = j+1
                            for k in range(j+1, len(s)):
                                if s[k].isdigit():
                                    mul += s[k]
                                else:
                                    break
                            mul = int(mul) if mul else 1
                            res = rec(subformula, mul)
                            c += res
                            i = k-1
                            break
                i += 1
            if var: 
                c[var] += max(1, cnt)
            for k in c:
                c[k] *= factor
            # print(s, factor, c)
            return c

        c = rec(formula, 1)
        # print(c)
        return ''.join(k+(str(c[k]) if c[k] > 1 else '') for k in sorted(c) if k)
