class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1 # xxxxxxx & 00000001 -->bit = 1 if 1 & 1 = 1 else 0
            n = n >> 1
        return count
