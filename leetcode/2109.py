class Solution:
    def addSpaces(self, st: str, spaces: List[int]) -> str:
        s = set([0] + spaces + [len(st)])
        s = list(sorted(s))

        ss = []
        for a, b in zip(s, s[1:]):
            ss.append(st[a:b])
        
        xx = " ".join(ss)
        if spaces[0] == 0:
            xx = ' ' + xx
        return xx
