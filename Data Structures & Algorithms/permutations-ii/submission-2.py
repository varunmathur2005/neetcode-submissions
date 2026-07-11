class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    sol.append(n)
                    backtrack()
                    sol.pop()
                    count[n] += 1
            
        backtrack()
        return res

