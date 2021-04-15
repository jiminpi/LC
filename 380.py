class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.table:
            return False
        else:
            self.nums.append(val)
            self.table[val] = len(self.nums) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.table:
            return False
        else:
            tmp_idx = self.table[val]
            self.nums[tmp_idx] = self.nums[-1]
            self.table[self.nums[-1]] = tmp_idx
            self.nums.pop()
            del self.table[val]
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # idx = random.randint(0, len(self.nums)-1)
        # return self.nums[idx]
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
