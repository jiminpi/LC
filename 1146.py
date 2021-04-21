class SnapshotArray:

    def __init__(self, length: int):
        self.vals_ = a = [{} for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.vals_[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        val = self.vals_[index].get(snap_id)
        while not val:
            if snap_id == 0:
                return 0
            else:
                snap_id -= 1
                val = self.vals_[index].get(snap_id)
        return val


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
