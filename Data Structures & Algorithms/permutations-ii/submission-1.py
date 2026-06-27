class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in count:
                if count[n] > 0:
                    sol.append(n)
                    count[n] -= 1
                    backtrack()
                    sol.pop()
                    count[n] += 1
        
        backtrack()
        return res

