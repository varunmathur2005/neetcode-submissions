class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curmax, curmin = nums[0], 1, 1
        for n in nums:
            temp = n * curmax
            curmax = max(n, curmax * n, curmin * n)
            curmin = min(n, temp, curmin * n)
            res = max(curmax, res)
        
        return res