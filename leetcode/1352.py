class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.zeros = []

    def add(self, num: int) -> None:
        if not num:
            self.arr.append(num)
            self.zeros.append(len(self.arr)-1)
        else:
            if not self.arr or not self.arr[-1]:
                self.arr.append(num)
                return
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        # print(self.arr, self.zeros, k)
        k = len(self.arr) - k
        idx = bisect_left(self.zeros, k)
        if idx < len(self.zeros):
            return 0
        # print(self.arr[-1], self.arr[k-1], k-1)
        return self.arr[-1]//(self.arr[k-1] if k-1 >= 0 and self.arr[k-1] else 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
