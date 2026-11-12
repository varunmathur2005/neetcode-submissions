class FreqStack:
    def __init__(self):
        self.count = {} # element: count
        self.maxf = 0 # count of most frequent element
        self.stacks = {} # count: [stack]

    def push(self, val: int) -> None:
        val_count = 1 + self.count.get(val, 0)
        self.count[val] = val_count
        if val_count > self.maxf:
            self.maxf = val_count
            self.stacks[val_count] = []
        self.stacks[val_count].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxf].pop()
        self.count[res] -= 1
        if not self.stacks[self.maxf]:
            self.maxf -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()