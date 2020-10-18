
    def __init__(self):
        self.stk = []

    def next(self, p: int) -> int:
        cnt = 1
        while self.stk and self.stk[-1][0] <= p:
            cnt += self.stk.pop()[1]
        self.stk.append((p, cnt))
        return cnt
