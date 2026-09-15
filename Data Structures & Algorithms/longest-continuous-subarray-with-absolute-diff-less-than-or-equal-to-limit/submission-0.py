class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap = []
        maxHeap = []
        l = 0
        max_window = 0

        for r in range(len(nums)):
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                l += 1
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                while minHeap and minHeap[0][1] < l:
                    heapq.heappop(minHeap)


            max_window = max(max_window, r - l + 1)
        
        return max_window