class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class LinkedList:
    def __init__(self):
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0
    
    def length(self):
        return self.size
    
    def pushRight(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
        self.size += 1
    
    def pop(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.prev = node.next = None
        self.size -= 1

    def popLRU(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCount = 0
        # key --> node
        self.nodeMap = {} 
        self.listMap = defaultdict(LinkedList)
    
    def counter(self, node):
        count = node.freq
        self.listMap[count].pop(node)
        if count == self.lfuCount and self.listMap[count].length() == 0:
            self.lfuCount += 1
        
        node.freq += 1
        self.listMap[count + 1].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return 
        
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return 
        
        if len(self.nodeMap) == self.cap:
            node = self.listMap[self.lfuCount].popLRU()
            self.nodeMap.pop(node.key)
        
        node = Node(key, value)
        self.nodeMap[key] = node
        self.listMap[1].pushRight(node)
        self.lfuCount = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)