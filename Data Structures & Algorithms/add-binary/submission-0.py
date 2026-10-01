class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0 
            sumDigit = digitA + digitB + carry
            res.append(sumDigit % 2)
            carry = sumDigit // 2
            i, j = i - 1, j - 1
        
        res.reverse()
        return "".join(map(str, res))

