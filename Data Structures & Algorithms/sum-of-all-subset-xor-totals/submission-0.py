class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res, sol = 0, 0

        n = len(nums)

        if n == 0:
            return 0

        def backtrack(i):
            nonlocal res, sol
            
            if i == len(nums):
                res += sol 
                return 
            
            backtrack(i + 1)

            sol ^= nums[i]
            backtrack(i + 1)
            sol ^= nums[i]

        backtrack(0)
        return res