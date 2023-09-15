class Solution:
    def myAtoi(self, s: str) -> int:
        MIN,MAX = -2**31, 2**31 - 1
        sign = +1
        num = 0
        for i,x in enumerate(s.lstrip()):
            if i==0 and x=="-": sign = -1
            elif i==0 and x=="+": continue
            elif x.isdigit(): num = 10*num + int(x)
            else: break
        return max(min(MAX, sign*num), MIN)