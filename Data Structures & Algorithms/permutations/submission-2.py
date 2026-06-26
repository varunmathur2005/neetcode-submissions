class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in nums:
                if n not in sol:
                    sol.append(n)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res
