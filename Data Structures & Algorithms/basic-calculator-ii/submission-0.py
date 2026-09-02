class Solution:
    def calculate(self, s: str) -> int:
        res = []
        op = "+"
        num = 0

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-/*" or i == len(s) - 1:
                if op == "+":
                    res.append(num)
                elif op == "-":
                    res.append(-num)
                elif op == "*":
                    res[-1] *= num
                elif op == "/":
                    res[-1] = int(res[-1] / num) 
                op = c
                num = 0

        return sum(res)
            
            