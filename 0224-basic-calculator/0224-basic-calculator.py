class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        result = 0
        sign = 1
        stack = []
        for i,x in enumerate(s):
            if x.isdigit():
                num = num*10 + int(x)
                
            if x in "+-)" or i == len(s)-1:
                result += sign*num
                sign = 1
                num = 0
                
            if   x == "+": sign =  1
            elif x == "-": sign = -1
            elif x == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif x == ")":
                sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + sign*result
                sign = 1
                num = 0
        return result