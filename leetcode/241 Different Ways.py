class Solution:
    def diffWaysToCompute(self, ex: str) -> List[int]:
        def solve(a, o, b):
            if o == '+':
                return int(a) + int(b)
            if o == '-':
                return int(a) - int(b)
            return int(a) * int(b)

        @cache
        def rec(l, r):
            if l + 1 >= r:
                return [int(ex[l:r+1])]
            ret = []
            for i in range(l, r+1):
                if ex[i].isdigit():
                    continue
                ll = rec(l, i-1)
                rr = rec(i+1, r)

                for x in ll:
                    for y in rr:
                        ret.append(solve(x, ex[i], y))
            return ret
        
        return rec(0, len(ex)-1)
