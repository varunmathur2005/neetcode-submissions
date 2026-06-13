class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda t: t[1])

        minHeap = [] # [end, number of passenger]
        curCap = 0
        for t in trips:
            curPas, start, end = t
            while minHeap and minHeap[0][0] <= start:
                curCap -= minHeap[0][1]
                heapq.heappop(minHeap)
            curCap += curPas
            if curCap > capacity:
                return False
            
            heapq.heappush(minHeap, [end, curPas])
        
        return True