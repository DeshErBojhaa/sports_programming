def __init__(self, A: List[int]):
        self.c = []
        self.v = []
        for i, x in enumerate(A[::-1]):
            if i%2: 
                self.c.append(x)
            else:
                self.v.append(x)
            

    def next(self, n: int) -> int:
        print(self.c, self.v)
        cnt, x = 0, -1
        while self.c and self.c[-1] + cnt < n:
            cnt += self.c.pop()
            x = self.v.pop()
        if not self.c:
            return -1
        cnt += self.c.pop()
        x = self.v.pop()
        
        if cnt > n:
            self.c.append(cnt-n)
            self.v.append(x)
        return x
