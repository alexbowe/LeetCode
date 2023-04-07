class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -2**31, 2**31-1
        result = 0
        sign = 1
        for i,x in enumerate(s.lstrip()):
            if   i == 0 and x == "-": sign = -1
            elif i == 0 and x == "+": sign =  1
            elif x.isdigit(): result = result*10 + int(x)
            else: break
        return min(MAX, max(MIN, sign*result))