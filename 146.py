class nodelist:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = nodelist(None, None)
        self.tail = nodelist(None, None)
        self.mem = {}
        self.count = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.mem:
            node = self.mem[key]
            self.moveToFront_(node)
            return node.val
        else:
            return -1
    
    def moveToFront_(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.addToFront_(node)

    def addToFront_(self, node):
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        tmp.prev = node
        node.prev = self.head

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self.mem[key].val = value
            self.moveToFront_(self.mem[key])
        else:
            if self.count == self.capacity:
                self.removeLast_()
            else:
                self.count += 1
            self.mem[key] = nodelist(key, value)
            self.addToFront_(self.mem[key])
        
    
    def removeLast_(self):
        node = self.tail.prev.key
        del self.mem[node.key]
        self.tail.prev = node.prev
        node.prev.next = self.tail
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
