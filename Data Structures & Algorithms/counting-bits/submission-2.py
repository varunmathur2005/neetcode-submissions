class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one_bits(num):
            res = 0
            while num:
                res += num & 1
                num = num >> 1
            return res
        
        res = []
        for i in range(n + 1):
            res.append(count_one_bits(i))
        
        return res