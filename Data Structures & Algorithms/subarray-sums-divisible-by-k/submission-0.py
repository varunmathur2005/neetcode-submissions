class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        
        res = 0
        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            remainder = prefix_sum % k
            res += remainder_count[remainder]
            remainder_count[remainder] += 1 
        
        return res