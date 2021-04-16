class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(list)
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.table:
            flag = False
        else:
            flag = True
        
        self.table[val].append(len(self.nums))
        self.nums.append([val, len(self.table[val])-1])
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.table or len(self.table[val]) == 0:
            return False
        else:
            remove_idx = self.table[val][-1]
            last_val, last_idx = self.nums[-1]
            self.table[last_val][last_idx] = remove_idx
            self.nums[remove_idx] = [last_val, last_idx]
            self.table[val].pop()
            self.nums.pop()
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.nums)[0]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
