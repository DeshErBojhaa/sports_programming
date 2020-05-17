# 384. Shuffle an Array
from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.n = nums[::1]
        self.shuffeled = nums[::1]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.n

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        if not self.n:
            return self.n
        
        x = self.shuffeled
        for i in range(3):
            ind = randint(0, len(x)-1)
            x[0], x[ind] = x[ind], x[0]
        return x


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
