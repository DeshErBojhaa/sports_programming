# 1472. Design Browser History
class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.cur + 1] + [url]
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, len(self.arr) - 1)
        return self.arr[self.cur]
            


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
