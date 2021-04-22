class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.nums = []

    def push(self, x: int) -> None:
        if len(self.nums) < self.maxSize:
            self.nums.append(x)

    def pop(self) -> int:
        if self.nums:
            return self.nums.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        n = min(k, len(self.nums))
        for i in range(n):
            self.nums[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
