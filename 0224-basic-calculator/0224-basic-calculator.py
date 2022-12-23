class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        num = 0
        result = 0
        
        for i,x in enumerate(s):
            if x.isdigit():
                num = num*10 + int(x)
                
            if x in "+-)" or i == len(s)-1:
                result += sign*num
                sign, num = 1, 0
            
            if   x == "-": sign = -1
            elif x == "+": sign =  1
            elif x == "(":
                stack.extend([result, sign])
                result, sign = 0, 1
            elif x == ")":
                sign, prev_result = stack.pop(), stack.pop()
                result = prev_result + sign*result
                sign = 1
        return result