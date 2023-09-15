class Solution:
    def myAtoi(self, s: str) -> int:
        MIN,MAX = -2**31, 2**31 - 1
        sign, num = +1, 0
        for i,x in enumerate(s.lstrip()):
            if   i==0 and x=="-": sign = -1
            elif i==0 and x=="+": sign = +1
            elif x.isdigit(): num = 10*num + int(x)
            else: break
        return max(min(MAX, sign*num), MIN)