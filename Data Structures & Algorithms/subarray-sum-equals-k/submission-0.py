class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = res = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 # empty subarray
        for n in nums:
            cur_sum += n
            need = cur_sum - k
            res += prefix_count[need]
            prefix_count[cur_sum] += 1
        
        return res
