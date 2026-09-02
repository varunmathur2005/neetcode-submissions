class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [max(n, 0) for n in nums]
        for i in range(len(nums)):
            cur_num = abs(nums[i])
            if 1 <= cur_num <= len(nums):
                if nums[cur_num - 1] > 0: 
                    nums[cur_num - 1] *= -1
                elif nums[cur_num - 1] == 0:
                    nums[cur_num - 1] = -1 * (len(nums) + 1)
        
        print(nums)
        for j in range(1, len(nums) + 1):
            if nums[j - 1] >= 0:
                return j


        return len(nums) + 1

