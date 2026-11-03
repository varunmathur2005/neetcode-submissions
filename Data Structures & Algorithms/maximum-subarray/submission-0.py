class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        cur_sum = 0 
        for n in nums:
            cur_sum += n
            if cur_sum < 0 :
                cur_sum = 0
            else:
                res = max(res, cur_sum)

        return res