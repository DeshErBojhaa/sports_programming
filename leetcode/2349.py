class NumberContainers:

    def __init__(self):
        self.idx_val = {}
        self.indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx_val[index] = number
        heappush(self.indices[number], index)        

    def find(self, number: int) -> int:
        l = self.indices[number]
        while l:
            idx = l[0]
            if self.idx_val[idx] == number:
                self.indices[number] = l
                return idx
            heappop(l)
            
        self.indices[number] = l
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
