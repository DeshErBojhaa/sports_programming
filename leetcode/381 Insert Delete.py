class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = [] # list to store values
        self.indices = {} # hash map to store indices of each value

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.vals.append(val) # add value to end of list
        if val in self.indices: # if value already exists in hash map
            self.indices[val].add(len(self.vals)-1) # add index to set of indices
            return False
        else:
            self.indices[val] = {len(self.vals)-1} # create new set with index
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.indices: # if value doesn't exist in hash map
            return False
        
        index = self.indices[val].pop() # get an index of the value and remove it from set
        last_val = self.vals[-1] # get the last value in list
        if index != len(self.vals)-1: # if index is not the last index
            self.vals[index] = last_val # replace value at index with last value
            self.indices[last_val].discard(len(self.vals)-1) # remove last index from set
            self.indices[last_val].add(index) # add index to set of last value
        
        self.vals.pop() # remove last value from list
        if not self.indices[val]: # if set of indices is empty
            del self.indices[val] # remove key from hash map
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.vals) # return a random value from the list
