# 380. Insert Delete GetRandom O(1)
from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        b = False
        if val not in self.s:
            b = True
        self.s.add(val)
        return b

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.s:
            return False
        self.s.discard(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        arr = []
        while self.s and len(arr) < 5:
            v = self.s.pop()
            arr.append(v)
        self.s.update(arr)
        return choice(arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
