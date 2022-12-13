class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        
        sign, value = 1, 0
        for i,x in enumerate(s.lstrip(" ")):
            if i == 0 and x == "-": sign = -1
            elif i == 0 and x == "+": sign = 1
            elif x.isdigit(): value = value*10 + int(x)
            else: break
        return max(min(MAX, sign * value), MIN)