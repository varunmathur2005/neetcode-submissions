class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            need = prefix - goal
            res += prefix_count[need]
            prefix_count[prefix] += 1
        
        return res
