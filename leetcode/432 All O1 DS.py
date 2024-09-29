class AllOne:

    def __init__(self):
        self.c = Counter()

    def inc(self, key: str) -> None:
        self.c[key] += 1

    def dec(self, key: str) -> None:
        self.c[key] -= 1
        if self.c[key] == 0:
            del self.c[key]

    def getMaxKey(self) -> str:
        if len(self.c) == 0:
            return ''
        return self.c.most_common(1)[0][0]

    def getMinKey(self) -> str:
        m, c = inf, ''
        for k, v in self.c.items():
            if v < m:
                m = v
                c = k
        return c
