class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # (index, value)
        l = 0

        for r, n in enumerate(nums):
            while q and q[-1][1] < n:
                q.pop()
            q.append((r, n))
            if l > q[0][0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(q[0][1])
                l += 1
        
        return res
