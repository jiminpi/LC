class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        # trick: default freq is 0. faciliate adding new node. the increaseFrequency_() function will make the frquency to 1.
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key
    
    def insertAtNext(self, nex):
        # insert nex after the current node
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex

def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = collections.defaultdict(create_linked_list)
        self.keyMap = {}
    
    def delete_(self, node):
        # delete node from its current frequency list 
        # also called when adding a new node. so there is an "if" here
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
                del self.freqMap[node.freq]
            return node.key

    def increaseFrequency_(self, node):
        self.delete_(node)
        node.freq += 1
        self.freqMap[node.freq][0].insertAtNext(node)
        if self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq        
        elif node.freq == 1:
            self.minFreq = 1
        
        
    def get(self, key: int) -> int:
        if key in self.keyMap:
            node = self.keyMap[key]
            self.increaseFrequency_(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            # trick: the input capacity can be 0 in this problem
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
                if self.size > self.capacity:
                    self.size -= 1
                    deleted_key = self.delete_(self.freqMap[self.minFreq][-1].pre)
                    del self.keyMap[deleted_key]
            self.increaseFrequency_(node)




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
