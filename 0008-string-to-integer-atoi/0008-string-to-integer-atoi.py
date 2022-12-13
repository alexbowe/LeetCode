class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        
        whitespace = " "
        s = s.lstrip(whitespace)
        
        value = 0
        sign = 1
        for i,x in enumerate(s):
            if i == 0 and x == "-": sign = -1
            elif i == 0 and x == "+": sign = 1
            elif x.isdigit(): value = value*10 + int(x)
            else: break
        return max(min(MAX, sign * value), MIN)