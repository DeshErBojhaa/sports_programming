class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bit = [0] * (self.n+1)
        self.arr = nums
        
        for i, v in enumerate(nums):
            ind = i + 1
            while ind <= self.n:
                self.bit[ind] += v
                ind += ind&-ind
        # print(self.bit)

    def update(self, i: int, val: int) -> None:
        diff, self.arr[i] = val - self.arr[i], val
        i += 1
        while i <= self.n:
            self.bit[i] += diff
            i += i&-i
    

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        j += 1
        while j > 0:
            ans += self.bit[j]
            j -= j&-j
        
        while i > 0:
            ans -= self.bit[i]
            i -= i&-i
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
