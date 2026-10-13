class MedianFinder:

    def __init__(self):
        # self.small = maxHeap ; self.large = minHeap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        '''
        We could have added the num to lets say self.small but then
        we would have to check if -self.small[0] > self.large[0]
        instead when we are adding we check if the curr value is bigger
        than the biggest value in self.large then we know it must go to self.large
        and then we can balance the heaps
        '''
        # All element in self.large > all elements in self.small
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        # Heap balancing
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        elif len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)


    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]
        
        return (self.large[0] - self.small[0]) / 2

